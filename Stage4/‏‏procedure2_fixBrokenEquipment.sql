-- =============================================
-- Stored Procedure: Automated Equipment Repair System
-- This procedure identifies and repairs all broken equipment in the gym
-- Provides comprehensive logging and error handling for maintenance operations
-- =============================================

CREATE OR REPLACE PROCEDURE fix_broken_equipment()
LANGUAGE plpgsql
AS $$
DECLARE
    -- Cursor to iterate through all broken equipment
    -- Only selects equipment with condition 'F' (Faulty/Broken)
    eq_cursor CURSOR FOR
        SELECT eq_id, eq_name, condition, age_restriction
        FROM equipment
        WHERE condition = 'F';  -- Filter for broken equipment only

    -- Record variable to hold cursor data
    eq_rec RECORD;
    
    -- Counter to track number of repaired items
    fixed_count INTEGER := 0;
BEGIN
    -- Log the start of repair operations
    RAISE NOTICE 'Starting broken equipment repair...';

    -- Iterate through each piece of broken equipment
    FOR eq_rec IN eq_cursor LOOP
        -- Update equipment status from 'F' (Faulty) to 'T' (True/Working)
        -- This simulates the repair process
        UPDATE equipment
        SET condition = 'T'
        WHERE eq_id = eq_rec.eq_id;

        -- Increment counter for tracking progress
        fixed_count := fixed_count + 1;
        
        -- Log each successful repair with equipment details
        RAISE NOTICE 'Fixed equipment: % (ID: %)', eq_rec.eq_name, eq_rec.eq_id;
    END LOOP;

    -- Provide summary feedback based on results
    IF fixed_count = 0 THEN
        -- No broken equipment found - all equipment is functional
        RAISE NOTICE 'No broken equipment found.';
    ELSE
        -- Report total number of repairs completed
        RAISE NOTICE 'Total fixed equipment: %', fixed_count;
    END IF;

-- Comprehensive error handling
-- Catches any unexpected errors during the repair process
EXCEPTION
    WHEN OTHERS THEN
        -- Log error details and re-raise as a more specific exception
        RAISE EXCEPTION 'Error during equipment fix: %', SQLERRM;
END;
$$;