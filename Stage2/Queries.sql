-------------SELECT QUERIES------------------   

-- 1:
-- Returns all male trainers, including their ID, name, age, and experience level.
-- The results are sorted first by experience level (ascending) and then alphabetically by name.
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


-- 2:
-- Returns the number of classes each trainer is assigned to teach, along with their name.
-- The results are ordered by the number of classes in descending order.
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


-- 3:
-- Returns the list of members whose subscriptions are set to expire next month.
-- The results are ordered by the expiration date in ascending order.
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


-- 4:
-- Returns details of all classes scheduled for today.
-- Includes day of the week, gender (class attribute), class hour, class type, trainer ID and experience level, and room name.
SELECT 
    c.DayInWeek,
    c.Gender,
    c.HourC,
    ct.NameType,
    t.Id AS TrainerId,
    t.ExperienceLevel,
    r.NameR AS RoomName
FROM
    Class c
JOIN
    ClassType ct ON c.IdCT = ct.IdCT
JOIN
    Trainer t ON c.Id = t.Id
JOIN
    Room r ON c.IdR = r.IdR
WHERE
    c.DayInWeek = TO_CHAR(CURRENT_DATE, 'FMDay')
ORDER BY
    c.HourC;


-- 5:
-- Returns all classes that member with ID = 1 is registered for.
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


-- 6:
-- Returns the list of rooms that are available today (i.e., not occupied by any class).
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


-- 7:
-- Returns the list of members registered to a specific class (class ID = 5).
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


-- 8:
-- Returns all classes whose minimum age requirement is suitable for a 19-year-old participant.
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
    CT.MinAge <= 19;



-------------DELETE QUERIES------------------   

--1:
-- Delete trainers with low experience (level 1) who are not assigned to any class
DELETE FROM Trainer
WHERE ExperienceLevel = 1
AND Id NOT IN (
  SELECT DISTINCT Id
  FROM Class
);

--2:
-- Delete members whose membership expired more than one year ago
-- and who are over 30 years old
DELETE FROM Member
WHERE ExpirationDate < CURRENT_DATE - INTERVAL '1 year'
  AND Id IN (
    SELECT Id FROM Person
    WHERE DateOfBirth <= CURRENT_DATE - INTERVAL '30 years'
  );

--3:
-- Delete classes that had no registered members in the past two years
DELETE FROM Class
WHERE IdC NOT IN (
    SELECT DISTINCT r.IdC
    FROM registers_for r
    JOIN Member m ON r.Id = m.Id
    WHERE m.RegistrationDate >= CURRENT_DATE - INTERVAL '2 years'
);


-------------UPDATE QUERIES------------------   
-- Update 1
-- Members whose membership duration is longer than two years will receive a bonus: an extension of 2 months
UPDATE Member
SET ExpirationDate = ExpirationDate + INTERVAL '2 months'
WHERE ExpirationDate - RegistrationDate > 365;

-- Update 2
-- Increase experience level of trainers by 1 if they conducted more than 100 classes in the past year
UPDATE Trainer
SET ExperienceLevel = LEAST(ExperienceLevel + 1, 3)
WHERE Id IN (
  SELECT Id
  FROM Class
  GROUP BY Id
  HAVING COUNT(*) * 4 * 12 >= 100
);

-- Update 3
-- Replace broken equipment with IdE = 58 with another working equipment of the same name that is not assigned to any room (IdR IS NULL)
UPDATE Equipment AS e_good
SET IdR = (
  SELECT IdR FROM Equipment WHERE IdE = 58
)
WHERE e_good.Condition = 'T'
  AND e_good.IdR IS NULL
  AND e_good.NameE = (
    SELECT NameE FROM Equipment WHERE IdE = 58
  );



