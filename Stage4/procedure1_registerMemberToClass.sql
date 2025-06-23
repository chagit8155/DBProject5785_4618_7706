-- ============================================================================
-- STORED PROCEDURE: register_member_to_class
-- ============================================================================
-- Purpose: Register a member to a fitness class with comprehensive validation
-- Parameters:
--   p_course_id: ID of the course to register for
--   p_member_id: ID of the member to register
-- 
-- Features:
--   - Validates course existence
--   - Checks member validity and active membership
--   - Age restriction validation
--   - Room capacity validation
--   - Prevents duplicate registrations
--   - Automatically updates class registrant count
-- ============================================================================

CREATE OR REPLACE PROCEDURE register_member_to_class(
    p_course_id INTEGER,  -- Course ID parameter
    p_member_id INTEGER   -- Member ID parameter
)
LANGUAGE plpgsql
AS $$
DECLARE
    -- Record to store class information during iteration
    class_rec RECORD;
    
    -- Variable to store member's age
    v_member_age INTEGER;
    
    -- Flag to track if registration was successful
    v_registration_success BOOLEAN := FALSE;
    
    -- Variable to store error messages
    v_error_message TEXT := '';
BEGIN
    -- ========================================================================
    -- STEP 1: Validate course existence
    -- ========================================================================
    -- Check if the provided course ID exists in the Course table
    IF NOT EXISTS (SELECT 1 FROM Course WHERE course_id = p_course_id) THEN
        RAISE EXCEPTION 'Course ID % does not exist', p_course_id;
    END IF;

    -- ========================================================================
    -- STEP 2: Validate member and check active membership
    -- ========================================================================
    -- Get member's age and verify membership is active (not expired)
    -- Uses JOIN to connect Person and Member tables
    -- Calculates age using EXTRACT and AGE functions
    SELECT EXTRACT(YEAR FROM AGE(p.birth_date)) INTO v_member_age
    FROM Person p
    JOIN Member m ON p.person_id = m.person_id
    WHERE m.person_id = p_member_id
    AND m.expirationdate > CURRENT_DATE;  -- Only active memberships

    -- If no record found, member doesn't exist or membership expired
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Member % not found or membership expired', p_member_id;
    END IF;

    -- ========================================================================
    -- STEP 3: Search for suitable class and attempt registration
    -- ========================================================================
    -- Loop through all classes for the specified course
    -- Gather comprehensive class information including room capacity and requirements
    FOR class_rec IN
        SELECT c.timeslot_id, c.room_id, c.person_id as trainer_id, c.registrants,
               r.capacity as room_capacity, co.course_name, co.min_age,
               t.day, t.start_time
        FROM Class c
        JOIN Course co ON c.course_id = co.course_id      -- Get course details
        JOIN TimeSlot t ON c.timeslot_id = t.timeslot_id  -- Get schedule info
        JOIN Room r ON c.room_id = r.room_id              -- Get room capacity
        WHERE c.course_id = p_course_id
    LOOP
        -- ====================================================================
        -- VALIDATION 1: Age restriction check
        -- ====================================================================
        -- Skip this class if member doesn't meet minimum age requirement
        IF v_member_age < class_rec.min_age THEN
            CONTINUE;  -- Move to next class iteration
        END IF;

        -- ====================================================================
        -- VALIDATION 2: Room capacity check
        -- ====================================================================
        -- Skip if class is full (registrants >= room capacity)
        -- COALESCE handles NULL registrants by treating as 0
        IF COALESCE(class_rec.registrants, 0) >= class_rec.room_capacity THEN
            CONTINUE;  -- Move to next class iteration
        END IF;

        -- ====================================================================
        -- VALIDATION 3: Duplicate registration check
        -- ====================================================================
        -- Skip if member is already registered for this specific class
        -- Uses timeslot_id and room_id to uniquely identify the class
        IF EXISTS (
            SELECT 1 FROM registers_for
            WHERE person_id = p_member_id
            AND timeslot_id = class_rec.timeslot_id
            AND room_id = class_rec.room_id
        ) THEN
            CONTINUE;  -- Move to next class iteration
        END IF;

        -- ====================================================================
        -- REGISTRATION EXECUTION
        -- ====================================================================
        -- All validations passed - perform the actual registration
        
        -- Insert registration record
        INSERT INTO registers_for (person_id, timeslot_id, room_id)
        VALUES (p_member_id, class_rec.timeslot_id, class_rec.room_id);

        -- Update class registrant count
        -- Increment the number of registered members for this class
        UPDATE Class
        SET registrants = COALESCE(registrants, 0) + 1
        WHERE timeslot_id = class_rec.timeslot_id
        AND room_id = class_rec.room_id;

        -- Log successful registration with details
        RAISE NOTICE 'Member % successfully registered to class % on % at %',
            p_member_id, class_rec.course_name, class_rec.day, class_rec.start_time;

        -- Mark registration as successful and exit loop
        v_registration_success := TRUE;
        EXIT;  -- Exit the loop since registration is complete
    END LOOP;

    -- ========================================================================
    -- STEP 4: Handle case where no suitable class was found
    -- ========================================================================
    -- If we went through all classes without successful registration
    IF NOT v_registration_success THEN
        RAISE EXCEPTION 'No suitable class found for registration';
    END IF;

-- ============================================================================
-- EXCEPTION HANDLING
-- ============================================================================
-- Catch any unexpected errors during execution
EXCEPTION
    WHEN OTHERS THEN
        -- Store error message for logging
        v_error_message := SQLERRM;
        
        -- Log the error (won't stop execution rollback)
        RAISE NOTICE 'Error during registration: %', v_error_message;
        
        -- Re-raise the exception to ensure transaction rollback
        RAISE;
END;
$$;

-- ============================================================================
-- EXAMPLE USAGE AND TESTING
-- ============================================================================
-- The following block demonstrates how to test the procedure safely
-- Uses a transaction that can be rolled back to avoid permanent changes

BEGIN;  -- Start transaction for testing

-- Call the procedure with sample course and member IDs
-- Replace with actual IDs from your database
CALL register_member_to_class(33, 1010);

-- Verify the registration was created
-- This query shows the registration within the current transaction
SELECT * FROM registers_for
WHERE person_id = 1010;

-- Rollback to undo all changes (for testing purposes)
-- In production, use COMMIT instead to save changes
ROLLBACK;