-- =============================================
-- Trigger Function: Membership Expiration Alert System
-- This function monitors membership expiration dates and takes appropriate actions
-- Automatically cancels registrations for expired memberships and sends warnings
-- =============================================

CREATE OR REPLACE FUNCTION check_membership_expiration()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    -- Variable to store the member's full name
    person_name_var VARCHAR(30);
    
    -- Number of days until membership expires
    days_until_expiry INTEGER;
    
    -- Count of active registrations for this member
    registrations_count INTEGER;
BEGIN
    -- Retrieve member's name from person table using person_id
    SELECT person_name INTO person_name_var
    FROM person
    WHERE person_id = NEW.person_id;
    
    -- Calculate days remaining until expiration
    -- Positive number = days until expiry, Negative = days since expired
    days_until_expiry := NEW.expirationdate - CURRENT_DATE;
    
    -- Count how many active class registrations this member has
    SELECT COUNT(*) INTO registrations_count
    FROM registers_for
    WHERE person_id = NEW.person_id;
    
    -- Decision tree based on membership status
    IF NEW.expirationdate < CURRENT_DATE THEN
        -- Case 1: Membership has already expired
        -- Automatically cancel all registrations for expired member
        DELETE FROM registers_for WHERE person_id = NEW.person_id;
        
        -- Send critical warning about expired membership
        RAISE WARNING 'EXPIRED MEMBERSHIP: Member % (ID: %) membership has expired. All registrations cancelled.', 
                     person_name_var, NEW.person_id;
                     
    ELSIF days_until_expiry <= 7 AND days_until_expiry > 0 THEN
        -- Case 2: Membership expires within 7 days (early warning system)
        -- Send notification to alert about upcoming expiration
        RAISE NOTICE 'EXPIRATION WARNING: Member % (ID: %) membership expires in % days.', 
                     person_name_var, NEW.person_id, days_until_expiry;
    END IF;
    
    -- Return NEW record to allow the original operation to proceed
    RETURN NEW;
END;
$$;

-- =============================================
-- Trigger Definition: Membership Expiration Monitor
-- Automatically executes after INSERT or UPDATE operations on member table
-- Specifically monitors changes to the expiration date field
-- =============================================

CREATE OR REPLACE TRIGGER trigger_membership_expiration
    AFTER INSERT OR UPDATE OF expirationdate  -- Only fires when expirationdate changes
    ON member                                  -- Monitors the member table
    FOR EACH ROW                              -- Executes once per affected row
    EXECUTE FUNCTION check_membership_expiration();  -- Calls our validation function