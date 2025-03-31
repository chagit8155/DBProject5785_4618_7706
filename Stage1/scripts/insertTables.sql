INSERT INTO Person (Id, Gender, DateOfBirth, Name) VALUES
(1, 'M', '1990-05-15', 'David Cohen'),
(2, 'F', '1995-08-22', 'Sarah Levi'),
(3, 'M', '1988-12-10', 'Michael Israeli');

INSERT INTO Member (Id, RegistrationDate, ExpirationDate) VALUES
(1, '2024-01-01', '2025-01-01'),
(2, '2024-02-15', '2025-02-15'),
(3, '2024-03-20', '2025-03-20');

INSERT INTO Trainer (Id, ExperienceLevel) VALUES
(1, 3),
(2, 2),
(3, 1);
--macroo
INSERT INTO ClassType (IdCT, NameType, MinAge, RequiredExperience) VALUES
(101, 'Yoga', 16, 1),
(102, 'CrossFit', 18, 2),
(103, 'Pilates', 16, 1);

INSERT INTO Room (IdR, nameR, capacity) VALUES
(201, 'Pilatis', 30),
(202, 'Yoga Room', 20),
(203, 'Strength Zone', 25);

INSERT INTO Class (IdC, DayInWeek, Gender, HourC, IdCT, Id, IdR) VALUES
(401, 'Monday', 'M', '18', 101, 1, 201),
(402, 'Wednesday', 'F', '19', 102, 2, 202),
(403, 'Thursday', 'M', '20', 103, 3, 203);
--python
INSERT INTO Equipment (idE, Condition, NameE, IdR) VALUES
(301, 'T', 'Treadmill', 201),
(302, 'F', 'Dumbbells', 203),
(303, 'T', 'Yoga Mats', 202);

INSERT INTO certified_for (IdCT, Id) VALUES
(101, 1),
(102, 2),
(103, 3);

INSERT INTO registers_for (Id, IdC) VALUES
(1, 401),
(2, 402),
(3, 403);
--generatedata