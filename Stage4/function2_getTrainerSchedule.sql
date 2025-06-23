-- ============================================================================
-- FUNCTION 2: TRAINER SCHEDULE RETRIEVAL WITH REF CURSOR
-- ============================================================================
-- Purpose: Retrieve comprehensive schedule information for a specific trainer
-- 
-- Parameters:
--   trainer_id_param: ID of the trainer whose schedule to retrieve
--
-- Returns: REFCURSOR containing trainer's complete weekly schedule
--
-- Features:
--   - Validates trainer existence
--   - Retrieves trainer information (name, experience level)
--   - Counts total classes taught
--   - Returns detailed schedule with day-of-week ordering
--   - Includes class status based on registrations
-- ============================================================================

CREATE OR REPLACE FUNCTION get_trainer_schedule(trainer_id_param INTEGER)
RETURNS REFCURSOR
LANGUAGE plpgsql
AS $$
DECLARE
    -- ========================================================================
    -- VARIABLE DECLARATIONS
    -- ========================================================================
    
    -- Cursor name for returning schedule results
    schedule_cursor REFCURSOR := 'trainer_schedule_cursor';
    
    -- Record to store trainer basic information
    trainer_record RECORD;
    
    -- Counter for total classes taught by this trainer
    class_count INTEGER := 0;
    
BEGIN
    -- ========================================================================
    -- STEP 1: Validate trainer existence and get basic info
    -- ========================================================================
    
    -- Query to get trainer's name and experience level
    -- Joins Person table (for name) with Trainer table (for experience)
    SELECT p.person_name, t.experiencelevel 
    INTO trainer_record
    FROM person p 
    JOIN trainer t ON p.person_id = t.person_id 
    WHERE p.person_id = trainer_id_param;
    
    -- Check if trainer was found
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Trainer with ID % not found', trainer_id_param;
    END IF;
    
    -- ========================================================================
    -- STEP 2: Count total classes taught by this trainer
    -- ========================================================================
    
    -- Get total number of classes assigned to this trainer
    SELECT COUNT(*) INTO class_count
    FROM class c
    WHERE c.person_id = trainer_id_param;
    
    -- Log trainer information and class count
    RAISE NOTICE 'Trainer: %, Experience Level: %, Total Classes: %', 
                 trainer_record.person_name, trainer_record.experiencelevel, class_count;
    
    -- ========================================================================
    -- STEP 3: Build and open cursor with detailed schedule
    -- ========================================================================
    
    -- Open cursor with comprehensive schedule information
    OPEN schedule_cursor FOR
        SELECT 
            co.course_name,                    -- Name of the course/class
            ts.day,                           -- Day of the week
            ts.start_time,                    -- Class start time
            ts.end_time,                      -- Class end time
            r.room_name,                      -- Room where class is held
            c.registrants,                    -- Number of registered members
            CASE 
                WHEN c.registrants > 0 THEN 'Active'        -- Class has registrants
                ELSE 'No Registrants'                       -- Empty class
            END as status
        FROM class c
        JOIN course co ON c.course_id = co.course_id         -- Get course details
        JOIN timeslot ts ON c.timeslot_id = ts.timeslot_id   -- Get time information
        JOIN room r ON c.room_id = r.room_id                 -- Get room information
        WHERE c.person_id = trainer_id_param                 -- Filter for specific trainer
        ORDER BY 
            -- ================================================================
            -- Custom ordering to display schedule in weekly order
            -- ================================================================
            -- Convert day names to numbers for proper weekly ordering
            CASE ts.day
                WHEN 'Sunday' THEN 1
                WHEN 'Monday' THEN 2
                WHEN 'Tuesday' THEN 3
                WHEN 'Wednesday' THEN 4
                WHEN 'Thursday' THEN 5
                WHEN 'Friday' THEN 6
                WHEN 'Saturday' THEN 7
            END,
            ts.start_time;                    -- Secondary sort by start time
    
    -- Return the cursor reference
    RETURN schedule_cursor;
    
-- ============================================================================
-- EXCEPTION HANDLING
-- ============================================================================    
EXCEPTION
    -- Handle specific case where no data is found (shouldn't happen due to earlier check)
    WHEN NO_DATA_FOUND THEN
        RAISE EXCEPTION 'No data found for trainer ID %', trainer_id_param;
    
    -- Handle any other unexpected errors
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error retrieving trainer schedule: %', SQLERRM;
END;
$$;

-- ============================================================================
-- EXAMPLE USAGE AND TESTING
-- ============================================================================
-- Demonstrates how to call the function and process the returned cursor

DO $$
DECLARE
    -- Variables for cursor processing
    sched_cursor REFCURSOR;  -- Cursor returned by the function
    sched_record RECORD;     -- Record to hold each row of schedule data
BEGIN
    -- ========================================================================
    -- Call the function to get trainer schedule
    -- ========================================================================
    -- Replace 412 with actual trainer ID from your database
    sched_cursor := get_trainer_schedule(412);
    
    -- ========================================================================
    -- Process and display schedule results
    -- ========================================================================
    -- Loop through all classes in the trainer's schedule
    LOOP
        -- Fetch next class from the cursor
        FETCH sched_cursor INTO sched_record;
        
        -- Exit loop when no more classes
        EXIT WHEN NOT FOUND;
        
        -- Display detailed class information
        -- In a real application, you might INSERT into a report table
        -- or return this data to a client application
        RAISE NOTICE 'Course: %, Day: %, Time: % - %, Room: %, Registrants: %, Status: %',
            sched_record.course_name,      -- Course name
            sched_record.day,              -- Day of week
            sched_record.start_time,       -- Start time
            sched_record.end_time,         -- End time
            sched_record.room_name,        -- Room name
            sched_record.registrants,      -- Number of registrants
            sched_record.status;           -- Class status
    END LOOP;
    
    -- ========================================================================
    -- Cleanup: Close the cursor
    -- ========================================================================
    CLOSE sched_cursor;
END;
$$;

-- ============================================================================
-- ADDITIONAL NOTES ON FUNCTION DESIGN
-- ============================================================================
--
-- 1. ERROR HANDLING:
--    - Validates trainer existence before processing
--    - Provides specific error messages for different failure scenarios
--    - Uses structured exception handling
--
-- 2. PERFORMANCE CONSIDERATIONS:
--    - Uses JOINs instead of subqueries for better performance
--    - Efficient ordering using CASE statement for day-of-week
--    - Single query execution for cursor data
--
-- 3. DATA PRESENTATION:
--    - Orders results by day of week, then by time
--    - Includes status indicator for class activity
--    - Provides comprehensive class information in one view
--
-- 4. EXTENSIBILITY:
--    - Easy to add additional fields to the cursor query
--    - Can be modified to filter by date ranges
--    - Supports different output formats through cursor processing
-- ============================================================================