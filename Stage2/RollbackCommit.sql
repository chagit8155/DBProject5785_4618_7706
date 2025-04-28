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

INSERT INTO Equipment (IdE, NameE, IdR)
VALUES (402, 'Treadmill', 1);

SELECT *
FROM Class
WHERE IdE = 402;
INSERT INTO Member (Id, RegistrationDate, ExpirationDate)
VALUES (402, '2025-05-01', '2025-04-01');

--1:
--returns all male trainers, including their ID, name, age, and experience level. The results are sorted first by experience level (ascending) and then alphabetically by name.
SELECT
  t.Id,
  p.NameP,
  DATE_PART('year', AGE(p.DateOfBirth)) AS Age,
  t.ExperienceLevel
FROM
  Trainer t
JOIN
  Person p ON t.Id = p.Id
WHERE
  p.Gender = 'M'
ORDER BY
  t.ExperienceLevel ASC,
  p.NameP ASC;



--2:
-- returns the number of classes each trainer is assigned to teach, along with their name, ordered by the number of classes in descending order.
SELECT 
  T.Id AS TrainerId,
  P.NameP AS TrainerName,
  COUNT(*) AS WeeklyClasses
FROM 
  Trainer T
JOIN 
  Person P ON T.Id = P.Id
JOIN --LEFT 
  Class C ON C.Id = T.Id
GROUP BY 
  T.Id, P.NameP
ORDER BY 
  WeeklyClasses DESC; 


--3:
-- returns the list of members whose subscriptions are set to expire next month, ordered by the expiration date in ascending order.
SELECT 
  M.Id AS MemberId,
  P.NameP AS MemberName,
  M.ExpirationDate
FROM 
  Member M
JOIN 
  Person P ON M.Id = P.Id
WHERE 
  EXTRACT(MONTH FROM M.ExpirationDate) = EXTRACT(MONTH FROM CURRENT_DATE + INTERVAL '1 month')
  AND EXTRACT(YEAR FROM M.ExpirationDate) = EXTRACT(YEAR FROM CURRENT_DATE + INTERVAL '1 month')
ORDER BY 
  M.ExpirationDate;

--פרטי השיעורים שמתקיימים היום
SELECT 
    c.DayInWeek,  -- יום השבוע שבו מתרחש השיעור
    c.Gender,  -- מזהה השיעור
    c.HourC,  -- השעה שבה מתרחש השיעור
    ct.NameType,  -- סוג השיעור
    t.Id AS TrainerId,  -- מזהה המדריך
    t.ExperienceLevel,  -- רמת הניסיון של המדריך
    r.NameR AS RoomName  -- שם החדר שבו השיעור מתרחש
FROM
    Class c
JOIN
    ClassType ct ON c.IdCT = ct.IdCT  -- חיבור לטבלת סוגי השיעורים
JOIN
    Trainer t ON c.Id = t.Id  -- חיבור לטבלת מדריכים
JOIN
    Room r ON c.IdR = r.IdR  -- חיבור לטבלת חדרים
WHERE
    c.DayInWeek = TO_CHAR(CURRENT_DATE, 'FMDay')-- c.DayInWeek = TO_CHAR(CURRENT_DATE, 'Day')  -- משווים את יום השבוע להיום
ORDER BY
    c.HourC;  -- מסדרים לפי שעה


--כל השיעורים שמנוי 123 רשום אליהם
SELECT 
    p.NameP AS MemberName,
    c.IdC AS ClassId,
    ct.NameType AS ClassType,
    c.DayInWeek,
    c.HourC,
    r.NameR AS RoomName
FROM 
    registers_for rf
JOIN 
    Member m ON rf.Id = m.Id
JOIN 
    Person p ON m.Id = p.Id
JOIN 
    Class c ON rf.IdC = c.IdC
JOIN 
    ClassType ct ON c.IdCT = ct.IdCT
JOIN 
    Room r ON c.IdR = r.IdR
WHERE 
    p.Id = 1;


INSERT INTO registers_for (Id, IdC)
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5);

--פרטי החדרים שפנויים היום 
SELECT 
    r.IdR,
    r.NameR,
    r.Capacity
FROM 
    Room r
WHERE 
    r.IdR NOT IN (
        SELECT DISTINCT c.IdR
        FROM Class c
        WHERE c.DayInWeek = TO_CHAR(CURRENT_DATE, 'FMDay')
    )
ORDER BY 
    r.NameR;


-- כמה גברים וכמה נשים מנויים פעילים

SELECT 
    p.Gender,
    COUNT(*) AS ActiveMembers
FROM 
    Member m
JOIN 
    Person p ON m.Id = p.Id
WHERE 
    m.ExpirationDate > CURRENT_DATE
GROUP BY 
    p.Gender;

--
	


--שיעור מסויים - אלו מנויים רשומין אליו
SELECT 
    p.Id,
    p.NameP,
    p.Gender,
    p.DateOfBirth
FROM 
    registers_for rf
JOIN 
    Member m ON rf.Id = m.Id
JOIN 
    Person p ON m.Id = p.Id
WHERE 
    rf.IdC = 5;
--להוסיף נתונים




--שיעורים שהסוג שיעור מתאים לגיל 19
SELECT 
    C.IdC, 
    C.DayInWeek, 
    C.HourC, 
    CT.NameType, 
	CT.MinAge,
    R.NameR
FROM 
    Class C
JOIN 
    ClassType CT ON C.IdCT = CT.IdCT
JOIN 
    Room R ON C.IdR = R.IdR
WHERE 
    CT.MinAge <= 19; -- סוג שיעור שמתאים לגיל 19 ומעלה

	

--דליט
--מנויים שפג תוקף המנוי שלהם
--מחיקת שיעורים בתנאי שלא נרשמו אליהם מנויים בשנתיים האחרונות.
--


--אפדייט
--עדכון רמת ניסיון של מדריכים
--עדכון תוקף המנוי כאשר הוא מקבל הנחה לאחר השתתפות בכמות מסוימת של שיעורים
-- מעבר ציוד של חדר מסוים לחדר אחר
--

















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

INSERT INTO Equipment (IdE, NameE, IdR)
VALUES (402, 'Treadmill', 1);

SELECT *
FROM Class
WHERE IdE = 402;
INSERT INTO Member (Id, RegistrationDate, ExpirationDate)
VALUES (402, '2025-05-01', '2025-04-01');

--1:
--returns all male trainers, including their ID, name, age, and experience level. The results are sorted first by experience level (ascending) and then alphabetically by name.
SELECT
  t.Id,
  p.NameP,
  DATE_PART('year', AGE(p.DateOfBirth)) AS Age,
  t.ExperienceLevel
FROM
  Trainer t
JOIN
  Person p ON t.Id = p.Id
WHERE
  p.Gender = 'M'
ORDER BY
  t.ExperienceLevel ASC,
  p.NameP ASC;



--2:
-- returns the number of classes each trainer is assigned to teach, along with their name, ordered by the number of classes in descending order.
SELECT 
  T.Id AS TrainerId,
  P.NameP AS TrainerName,
  COUNT(*) AS WeeklyClasses
FROM 
  Trainer T
JOIN 
  Person P ON T.Id = P.Id
JOIN --LEFT 
  Class C ON C.Id = T.Id
GROUP BY 
  T.Id, P.NameP
ORDER BY 
  WeeklyClasses DESC; 


--3:
-- returns the list of members whose subscriptions are set to expire next month, ordered by the expiration date in ascending order.
SELECT 
  M.Id AS MemberId,
  P.NameP AS MemberName,
  M.ExpirationDate
FROM 
  Member M
JOIN 
  Person P ON M.Id = P.Id
WHERE 
  EXTRACT(MONTH FROM M.ExpirationDate) = EXTRACT(MONTH FROM CURRENT_DATE + INTERVAL '1 month')
  AND EXTRACT(YEAR FROM M.ExpirationDate) = EXTRACT(YEAR FROM CURRENT_DATE + INTERVAL '1 month')
ORDER BY 
  M.ExpirationDate;





INSERT INTO registers_for (Id, IdC)
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5);




-- כמה גברים וכמה נשים מנויים פעילים

SELECT 
    p.Gender,
    COUNT(*) AS ActiveMembers
FROM 
    Member m
JOIN 
    Person p ON m.Id = p.Id
WHERE 
    m.ExpirationDate > CURRENT_DATE
GROUP BY 
    p.Gender;

--
UPDATE Member
SET ExpirationDate = ExpirationDate + INTERVAL '2 month'
WHERE EXTRACT(MONTH FROM ExpirationDate) = EXTRACT(MONTH FROM CURRENT_DATE + INTERVAL '1 month')
  AND EXTRACT(YEAR FROM ExpirationDate) = EXTRACT(YEAR FROM CURRENT_DATE + INTERVAL '1 month');

--








	
--דליט
--מנויים שפג תוקף המנוי שלהם


--מחיקת שיעורים בתנאי שלא נרשמו אליהם מנויים בשנתיים האחרונות.
DELETE FROM Class
WHERE IdC NOT IN (
    SELECT DISTINCT r.IdC
    FROM registers_for r
    JOIN Member m ON r.Id = m.Id
    WHERE m.RegistrationDate >= CURRENT_DATE - INTERVAL '2 years'
);


--


--אפדייט
--עדכון רמת ניסיון של מדריכים
--עדכון תוקף המנוי כאשר הוא מקבל הנחה לאחר השתתפות בכמות מסוימת של שיעורים
-- מעבר ציוד של חדר מסוים לחדר אחר
--









