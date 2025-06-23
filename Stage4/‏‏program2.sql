-- =============================================
-- Main Program: Calls fix_broken_equipment and get_trainer_schedule procedures
-- This program demonstrates the integration of equipment maintenance and trainer scheduling
-- =============================================

BEGIN;

DO $$
DECLARE
    -- Trainer ID for schedule retrieval (change to existing trainer ID)
    v_trainer_id INTEGER := 402;
    
    -- Cursor to iterate through trainer schedule results
    v_cursor REFCURSOR;
    
    -- Variables to store schedule information from cursor
    v_course_name TEXT;    -- Name of the course/class
    v_day TEXT;           -- Day of the week
    v_start TEXT;         -- Start time of the class
    v_end TEXT;           -- End time of the class
    v_room TEXT;          -- Room where class takes place
    v_reg NUMERIC;        -- Number of registered participants
    v_status TEXT;        -- Current status of the class
BEGIN
    -- Part A: Fix broken equipment
    -- This procedure automatically repairs all equipment marked as faulty ('F')
    CALL fix_broken_equipment();

    -- Part B: Display trainer schedule
    -- Retrieve and display the complete schedule for a specific trainer
    RAISE NOTICE 'Fetching schedule for trainer ID: %', v_trainer_id;
    
    -- Call function to get trainer schedule and return cursor
    v_cursor := get_trainer_schedule(v_trainer_id);

    -- Loop through all schedule entries for the trainer
    LOOP
        -- Fetch next row from cursor into variables
        FETCH NEXT FROM v_cursor INTO v_course_name, v_day, v_start, v_end, v_room, v_reg, v_status;
        
        -- Exit loop when no more rows are found
        EXIT WHEN NOT FOUND;
        
        -- Display formatted schedule information
        RAISE NOTICE 'Class: %, Day: %, Time: %-% | Room: %, Registrants: %, Status: %',
                     v_course_name, v_day, v_start, v_end, v_room, v_reg, v_status;
    END LOOP;

    -- Close cursor to free resources
    CLOSE v_cursor;

    -- Indicate successful completion of main program
    RAISE NOTICE 'Main program completed.';
END $$;

-- Rollback all changes (for testing purposes)
-- In production, use COMMIT instead to persist changes
ROLLBACK;