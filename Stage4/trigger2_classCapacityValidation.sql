-- =============================================
-- Trigger Function: Class Capacity Validation and Management
-- This comprehensive function manages room capacity limits and automatically updates
-- registration counts while preventing overbooking of fitness classes
-- =============================================

CREATE OR REPLACE FUNCTION validate_class_capacity()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    -- Maximum capacity of the room
    room_capacity_var INTEGER;
    
    -- Current number of people registered for the class
    current_registrants_var INTEGER;
    
    -- Descriptive information for logging and error messages
    course_name_var VARCHAR(50);   -- Name of the fitness course
    room_name_var VARCHAR(15);     -- Name/identifier of the room
    trainer_name_var VARCHAR(30);  -- Name of the assigned trainer
BEGIN
    -- Retrieve room capacity and name information
    -- Uses COALESCE to handle both INSERT/UPDATE scenarios
    SELECT capacity, room_name INTO room_capacity_var, room_name_var
    FROM room
    WHERE room_id = COALESCE(NEW.room_id, NEW.room_id, OLD.room_id);
    
    -- Handle INSERT operations (new registrations)
    IF TG_OP = 'INSERT' THEN
        -- Count current registrations for this specific class
        SELECT COUNT(*) INTO current_registrants_var
        FROM registers_for
        WHERE timeslot_id = NEW.timeslot_id AND room_id = NEW.room_id;
        
        -- Enforce capacity limits - prevent overbooking
        IF current_registrants_var > room_capacity_var THEN
            RAISE EXCEPTION 'Cannot register: Room % capacity exceeded. Capacity: %, Attempting to register: %', 
                           room_name_var, room_capacity_var, current_registrants_var;
        END IF;
        
        -- Update the class table with current registration count
        -- This maintains data consistency across related tables
        UPDATE class 
        SET registrants = current_registrants_var
        WHERE timeslot_id = NEW.timeslot_id AND room_id = NEW.room_id;
        
        -- Retrieve course and trainer information for detailed logging
        SELECT co.course_name, p.person_name 
        INTO course_name_var, trainer_name_var
        FROM class c
        JOIN course co ON c.course_id = co.course_id
        LEFT JOIN person p ON c.person_id = p.person_id
        WHERE c.timeslot_id = NEW.timeslot_id AND c.room_id = NEW.room_id;
        
        -- Early warning system: Alert when approaching 90% capacity
        -- Helps gym staff prepare for potentially full classes
        IF current_registrants_var >= (room_capacity_var * 0.9) THEN
            RAISE NOTICE 'CAPACITY WARNING: Class % in room % is nearly full (%/% capacity)', 
                         course_name_var, room_name_var, current_registrants_var, room_capacity_var;
        END IF;
        
        RETURN NEW;
        
    -- Handle DELETE operations (registration cancellations)
    ELSIF TG_OP = 'DELETE' THEN
        -- Recount registrations after deletion
        SELECT COUNT(*) INTO current_registrants_var
        FROM registers_for
        WHERE timeslot_id = OLD.timeslot_id AND room_id = OLD.room_id;
        
        -- Update class table to reflect the cancellation
        UPDATE class 
        SET registrants = current_registrants_var
        WHERE timeslot_id = OLD.timeslot_id AND room_id = OLD.room_id;
        
        -- Log the cancellation with updated capacity information
        RAISE NOTICE 'Registration cancelled. Current capacity: %/%', 
                     current_registrants_var, room_capacity_var;
        
        RETURN OLD;
        
    -- Handle UPDATE operations (modifications to existing registrations)
    ELSIF TG_OP = 'UPDATE' THEN
        -- Check if the registration is being moved to a different room
        IF OLD.room_id IS DISTINCT FROM NEW.room_id THEN
            -- Validate capacity in the new room before allowing the move
            SELECT COUNT(*) INTO current_registrants_var
            FROM registers_for
            WHERE timeslot_id = NEW.timeslot_id AND room_id = NEW.room_id;
            
            -- Prevent moves that would exceed new room's capacity
            IF current_registrants_var >= room_capacity_var THEN
                RAISE EXCEPTION 'Cannot move to room %: capacity exceeded (%/%)', 
                               room_name_var, current_registrants_var, room_capacity_var;
            END IF;
        END IF;
        
        RETURN NEW;
    END IF;
    
    -- Fallback return (should not be reached in normal operation)
    RETURN NULL;
    
-- Comprehensive error handling
EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error in class capacity validation: %', SQLERRM;
END;
$$;

-- =============================================
-- Trigger Definitions: Complete Coverage for Registration Management
-- These triggers ensure capacity validation occurs for all possible scenarios
-- =============================================

-- Trigger for new registrations
CREATE OR REPLACE TRIGGER trigger_class_capacity_insert
    AFTER INSERT ON registers_for        -- Fires after new registration is added
    FOR EACH ROW                         -- Executes once per new registration
    EXECUTE FUNCTION validate_class_capacity();

-- Trigger for registration cancellations
CREATE OR REPLACE TRIGGER trigger_class_capacity_delete
    AFTER DELETE ON registers_for        -- Fires after registration is removed
    FOR EACH ROW                         -- Executes once per cancelled registration
    EXECUTE FUNCTION validate_class_capacity();

-- Trigger for registration modifications
CREATE OR REPLACE TRIGGER trigger_class_capacity_update
    AFTER UPDATE ON registers_for        -- Fires after registration is modified
    FOR EACH ROW                         -- Executes once per updated registration
    EXECUTE FUNCTION validate_class_capacity();