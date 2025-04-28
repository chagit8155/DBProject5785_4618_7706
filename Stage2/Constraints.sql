--1:
-- Add a CHECK constraint to ensure that room capacity is between 1 and 200
ALTER TABLE Room
ADD CONSTRAINT chk_capacity_positive CHECK (Capacity > 0 AND Capacity <= 200);

--2:
-- Set a DEFAULT value of 'T' (True) for the Condition column in Equipment table
ALTER TABLE Equipment
ALTER COLUMN Condition SET DEFAULT 'T';

--3:
-- Add a CHECK constraint to ensure that ExpirationDate is after RegistrationDate for Members
ALTER TABLE Member
ADD CONSTRAINT chk_member_dates CHECK (ExpirationDate > RegistrationDate);
