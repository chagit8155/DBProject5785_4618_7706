-- =============================================
-- Main Program: Member Analytics and Class Registration System
-- This program demonstrates a two-part workflow:
-- 1. Generate comprehensive member analytics and statistics
-- 2. Attempt to register a member for a specific class
-- Uses transaction control to ensure data integrity
-- =============================================

BEGIN;

DO $$
DECLARE
    -- Analytics Section Variables
    -- Cursor to handle multiple rows of analytics data
    v_cursor REFCURSOR;
    
    -- Variables to store analytics results from the cursor
    v_analysis_type TEXT;    -- Type of analysis (e.g., 'attendance', 'participation')
    v_metric_name TEXT;      -- Name of the specific metric being measured
    v_metric_value NUMERIC;  -- Numerical value of the metric
    v_details TEXT;          -- Additional details or description

    -- Registration Section Variables
    -- Specific member and class for registration attempt
    v_member_id INTEGER := 33;    -- Target member ID for registration
    v_class_id INTEGER := 1010;   -- Target class ID for registration
BEGIN
    -- =============================================
    -- PART 1: MEMBER ANALYTICS GENERATION
    -- =============================================
    
    RAISE NOTICE '--- Starting Member Analytics ---';
    
    -- Call analytics function for member ID 18
    -- Second parameter is NULL, which likely means "analyze all aspects"
    -- Returns a cursor containing multiple analytics results
    v_cursor := analyze_member_statistics(18, NULL);

    -- Process all analytics results from the cursor
    LOOP
        -- Fetch next row of analytics data
        FETCH NEXT FROM v_cursor INTO v_analysis_type, v_metric_name, v_metric_value, v_details;
        
        -- Exit loop when no more analytics data is available
        EXIT WHEN NOT FOUND;
        
        -- Display formatted analytics information
        -- Shows the type of analysis, metric name, and calculated value
        RAISE NOTICE 'Analytics → Type: %, Metric: %, Value: %', 
            v_analysis_type, v_metric_name, v_metric_value;
    END LOOP;

    -- Clean up resources by closing the cursor
    CLOSE v_cursor;

    -- =============================================
    -- PART 2: CLASS REGISTRATION ATTEMPT
    -- =============================================
    
    RAISE NOTICE '--- Attempting Registration ---';
    
    -- Attempt to register member for specified class
    -- Wrapped in exception handling to gracefully handle failures
    BEGIN
        -- Call registration procedure with member and class IDs
        CALL register_member_to_class(v_member_id, v_class_id);
        
    EXCEPTION
        -- Handle any registration failures (capacity, conflicts, etc.)
        WHEN OTHERS THEN
            -- Log the specific error message without stopping execution
            RAISE NOTICE 'Registration failed: %', SQLERRM;
    END;

END $$;

-- =============================================
-- TRANSACTION CONTROL
-- =============================================

-- Roll back all changes made during this session
-- This is typically used for testing purposes to avoid permanent changes
-- In production, replace with COMMIT to persist all successful operations
ROLLBACK;