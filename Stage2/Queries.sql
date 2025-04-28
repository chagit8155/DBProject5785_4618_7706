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
