-- RollbackCommit.sql

-- Update the database and perform ROLLBACK

BEGIN;

-- Display the Room table before the update
SELECT * FROM Room;

-- Perform an update
UPDATE Room
SET NameR = 'BeforeRollback'
WHERE IdR = 1;

-- Display the Room table after the update
SELECT * FROM Room;

-- Perform ROLLBACK to revert the changes
ROLLBACK;

-- Display the Room table again to confirm the change was undone
SELECT * FROM Room;



-- Update the database and perform COMMIT

BEGIN;

-- Display the Room table before the next update
SELECT * FROM Room;

-- Perform another update
UPDATE Room
SET Capacity = 45
WHERE IdR = 1;

-- Display the Room after the update
SELECT * FROM Room WHERE IdR = 1;

-- Perform COMMIT to save the change permanently
COMMIT;

-- Display the Room table again to confirm the change was saved
SELECT * FROM Room;
