-- ============================================================================
-- FUNCTION 1: COMPREHENSIVE MEMBER ANALYTICS WITH COMPLEX PROCESSING
-- ============================================================================
-- Purpose: Analyze member data and return comprehensive statistics
-- Features: Cursors, Records, DML operations, Loops, Exceptions, Conditionals
-- 
-- Parameters:
--   p_min_age: Minimum age filter for analysis (default: 18)
--   p_membership_type: Filter by membership type (default: NULL for all types)
--
-- Returns: REFCURSOR containing analytical results
-- 
-- Analytics Provided:
--   - Age distribution analysis
--   - Membership type statistics  
--   - Active vs expired member counts
--   - Class registration patterns
--   - Average metrics and summaries
-- ============================================================================

CREATE OR REPLACE FUNCTION analyze_member_statistics(
    p_min_age INTEGER DEFAULT 18,           -- Minimum age filter
    p_membership_type VARCHAR DEFAULT NULL  -- Membership type filter (NULL = all)
) 
RETURNS REFCURSOR
LANGUAGE plpgsql
AS $$
DECLARE
    -- ========================================================================
    -- CURSOR DECLARATIONS
    -- ========================================================================
    
    -- Main cursor for iterating through filtered members
    -- Joins Person and Member tables to get complete member information
    member_cursor CURSOR FOR 
        SELECT m.person_id, p.person_name, p.birth_date, m.membership_type,
               EXTRACT(YEAR FROM AGE(p.birth_date)) AS age,  -- Calculate current age
               m.registrationdate, m.expirationdate
        FROM Member m
        JOIN Person p ON m.person_id = p.person_id
        WHERE EXTRACT(YEAR FROM AGE(p.birth_date)) >= p_min_age  -- Age filter
        AND (p_membership_type IS NULL OR m.membership_type = p_membership_type);  -- Type filter

    -- Parameterized cursor for counting class registrations per member
    classes_cursor CURSOR(member_id INTEGER) FOR
        SELECT COUNT(*) as class_count
        FROM registers_for rf
        WHERE rf.person_id = member_id;

    -- ========================================================================
    -- VARIABLE DECLARATIONS
    -- ========================================================================
    
    -- Record variables to store cursor results
    member_rec RECORD;       -- Stores member information from main cursor
    class_count_rec RECORD;  -- Stores class count from classes cursor

    -- Statistical counters
    v_total_members INTEGER := 0;    -- Total number of members processed
    v_active_members INTEGER := 0;   -- Members with active membership
    v_expired_members INTEGER := 0;  -- Members with expired membership
    v_avg_age NUMERIC := 0;          -- Average age of members
    v_total_classes INTEGER := 0;    -- Total class registrations across all members

    -- Return cursor for results
    v_result_cursor REFCURSOR := 'member_analytics_cursor';

BEGIN
    -- ========================================================================
    -- STEP 1: Initialize temporary results table
    -- ========================================================================
    
    -- Drop existing temporary table if it exists (cleanup)
    DROP TABLE IF EXISTS temp_member_analytics;
    
    -- Create temporary table to store analytical results
    -- Structure allows for categorized metrics with descriptions
    CREATE TEMP TABLE temp_member_analytics (
        analysis_type VARCHAR(50),   -- Category of analysis (e.g., 'Age Distribution')
        metric_name VARCHAR(100),    -- Specific metric name
        metric_value NUMERIC,        -- Numerical value of the metric
        details TEXT                 -- Descriptive text about the metric
    );

    -- ========================================================================
    -- STEP 2: Process each member and collect statistics
    -- ========================================================================
    
    -- Loop through all members matching the filter criteria
    FOR member_rec IN member_cursor LOOP
        -- Increment total member counter
        v_total_members := v_total_members + 1;

        -- ====================================================================
        -- Membership Status Analysis
        -- ====================================================================
        -- Categorize member as active or expired based on expiration date
        IF member_rec.expirationdate > CURRENT_DATE THEN
            v_active_members := v_active_members + 1;
        ELSE
            v_expired_members := v_expired_members + 1;
        END IF;

        -- ====================================================================
        -- Class Registration Count for Current Member
        -- ====================================================================
        -- Open parameterized cursor to count classes for this specific member
        OPEN classes_cursor(member_rec.person_id);
        FETCH classes_cursor INTO class_count_rec;
        CLOSE classes_cursor;

        -- Add to total class registrations counter
        v_total_classes := v_total_classes + COALESCE(class_count_rec.class_count, 0);

        -- ====================================================================
        -- Age Group Distribution Analysis
        -- ====================================================================
        -- Categorize members into age groups and update counters
        
        -- Young Adults (18-25)
        IF member_rec.age BETWEEN 18 AND 25 THEN
            -- Try to update existing record
            UPDATE temp_member_analytics 
            SET metric_value = metric_value + 1 
            WHERE metric_name = 'Young Adults (18-25)';
            
            -- If no existing record, create new one
            IF NOT FOUND THEN
                INSERT INTO temp_member_analytics VALUES 
                ('Age Distribution', 'Young Adults (18-25)', 1, 'Ages 18-25');
            END IF;
            
        -- Adults (26-40)
        ELSIF member_rec.age BETWEEN 26 AND 40 THEN
            UPDATE temp_member_analytics 
            SET metric_value = metric_value + 1 
            WHERE metric_name = 'Adults (26-40)';
            IF NOT FOUND THEN
                INSERT INTO temp_member_analytics VALUES 
                ('Age Distribution', 'Adults (26-40)', 1, 'Ages 26-40');
            END IF;
            
        -- Senior Adults (40+)
        ELSIF member_rec.age > 40 THEN
            UPDATE temp_member_analytics 
            SET metric_value = metric_value + 1 
            WHERE metric_name = 'Senior Adults (40+)';
            IF NOT FOUND THEN
                INSERT INTO temp_member_analytics VALUES 
                ('Age Distribution', 'Senior Adults (40+)', 1, 'Ages 40+');
            END IF;
        END IF;

        -- ====================================================================
        -- Membership Type Statistics
        -- ====================================================================
        -- Count members by membership type (Premium, Basic, etc.)
        UPDATE temp_member_analytics 
        SET metric_value = metric_value + 1 
        WHERE analysis_type = 'Membership Types' AND metric_name = member_rec.membership_type;
        
        -- Create new record if this membership type hasn't been seen before
        IF NOT FOUND THEN
            INSERT INTO temp_member_analytics VALUES 
            ('Membership Types', member_rec.membership_type, 1, 
             'Count of ' || member_rec.membership_type || ' members');
        END IF;
    END LOOP;

    -- ========================================================================
    -- STEP 3: Generate summary statistics and handle edge cases
    -- ========================================================================
    
    -- Handle case where no members match the criteria
    IF v_total_members = 0 THEN
        INSERT INTO temp_member_analytics VALUES 
        ('Error', 'No Members Found', 0, 'No members match the specified criteria');
    ELSE
        -- Calculate average age across all filtered members
        SELECT AVG(EXTRACT(YEAR FROM AGE(p.birth_date))) INTO v_avg_age
        FROM Member m
        JOIN Person p ON m.person_id = p.person_id
        WHERE EXTRACT(YEAR FROM AGE(p.birth_date)) >= p_min_age
        AND (p_membership_type IS NULL OR m.membership_type = p_membership_type);

        -- Insert comprehensive summary statistics
        INSERT INTO temp_member_analytics VALUES 
        ('Summary', 'Total Members', v_total_members, 'Total number of members analyzed'),
        ('Summary', 'Active Members', v_active_members, 'Members with valid membership'),
        ('Summary', 'Expired Members', v_expired_members, 'Members with expired membership'),
        ('Summary', 'Average Age', ROUND(v_avg_age, 2), 'Average age of all members'),
        ('Summary', 'Total Class Registrations', v_total_classes, 'Sum of all class registrations'),
        ('Summary', 'Avg Classes per Member', 
         CASE WHEN v_total_members > 0 THEN ROUND(v_total_classes::NUMERIC / v_total_members, 2) ELSE 0 END,
         'Average classes per member');
    END IF;

    -- ========================================================================
    -- STEP 4: Prepare and return results cursor
    -- ========================================================================
    
    -- Open cursor with organized results
    -- Orders by analysis type and metric name for consistent output
    OPEN v_result_cursor FOR 
        SELECT analysis_type, metric_name, metric_value, details 
        FROM temp_member_analytics 
        ORDER BY analysis_type, metric_name;

    -- Return the cursor reference
    RETURN v_result_cursor;

-- ============================================================================
-- EXCEPTION HANDLING
-- ============================================================================
-- Handle any unexpected errors during analysis
EXCEPTION
    WHEN OTHERS THEN
        -- Log error details in results table
        INSERT INTO temp_member_analytics VALUES 
        ('Error', 'System Error', -1, 'Error: ' || SQLERRM);
        
        -- Return cursor with error information
        OPEN v_result_cursor FOR 
            SELECT analysis_type, metric_name, metric_value, details 
            FROM temp_member_analytics;
        RETURN v_result_cursor;
END;
$$;

-- ============================================================================
-- EXAMPLE USAGE AND TESTING
-- ============================================================================
-- Demonstrates how to call the function and process results

DO $$
DECLARE
    -- Variables to hold cursor and result data
    v_cursor REFCURSOR;      -- Cursor returned by the function
    v_analysis_type TEXT;    -- Category of analysis
    v_metric_name TEXT;      -- Name of the metric
    v_metric_value NUMERIC;  -- Value of the metric
    v_details TEXT;          -- Description of the metric
BEGIN
    -- ========================================================================
    -- Call the analytics function
    -- ========================================================================
    -- Parameters: minimum age 18, all membership types (NULL)
    v_cursor := analyze_member_statistics(18, NULL);
    
    -- ========================================================================
    -- Process and display results
    -- ========================================================================
    -- Loop through all results in the cursor
    LOOP
        -- Fetch next row from cursor
        FETCH NEXT FROM v_cursor INTO v_analysis_type, v_metric_name, v_metric_value, v_details;
        
        -- Exit loop when no more rows
        EXIT WHEN NOT FOUND;

        -- Display the result using RAISE NOTICE
        -- In a real application, you might INSERT into a report table
        RAISE NOTICE 'Type: %, Metric: %, Value: %, Details: %',
                     v_analysis_type, v_metric_name, v_metric_value, v_details;
    END LOOP;
    
    -- ========================================================================
    -- Cleanup: Close the cursor
    -- ========================================================================
    CLOSE v_cursor;
END $$;