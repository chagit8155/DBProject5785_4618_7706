SELECT * FROM registers_for;
SELECT * FROM certified_for;
SELECT * FROM Class;
SELECT * FROM Equipment;
SELECT * FROM Trainer;
SELECT * FROM Member;
SELECT * FROM Room;
SELECT * FROM ClassType;
SELECT * FROM Person;

-- ספירת כמות הרשומות בכל טבלה
SELECT 'registers_for' AS table_name, COUNT(*) FROM registers_for;
SELECT 'certified_for' AS table_name, COUNT(*) FROM certified_for;
SELECT 'Class' AS table_name, COUNT(*) FROM Class;
SELECT 'Equipment' AS table_name, COUNT(*) FROM Equipment;
SELECT 'Trainer' AS table_name, COUNT(*) FROM Trainer;
SELECT 'Member' AS table_name, COUNT(*) FROM Member;
SELECT 'Room' AS table_name, COUNT(*) FROM Room;
SELECT 'ClassType' AS table_name, COUNT(*) FROM ClassType;
SELECT 'Person' AS table_name, COUNT(*) FROM Person;
