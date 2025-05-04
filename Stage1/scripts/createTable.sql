CREATE TABLE if not exists Person --
(
  Id NUMERIC(3) ,
  Gender VARCHAR(1) NOT NULL CHECK (Gender IN ('F', 'M')),
  DateOfBirth DATE NOT NULL CHECK (DateOfBirth <= CURRENT_DATE - INTERVAL '16 years'),
  Name VARCHAR(30),
  PRIMARY KEY (Id)
);

CREATE TABLE if not exists ClassType--
(
  IdCT NUMERIC(3) ,
  NameType VARCHAR(15) ,
  MinAge NUMERIC(2) NOT NULL CHECK (MinAge >= 16),
  RequiredExperience NUMERIC(1) NOT NULL  CHECK (RequiredExperience IN (1, 2, 3)),
  PRIMARY KEY (IdCT)
);

CREATE TABLE if not exists Member--
(
  RegistrationDate DATE,
  ExpirationDate DATE NOT NULL,
  Id NUMERIC(3),
  PRIMARY KEY (Id),
  FOREIGN KEY (Id) REFERENCES Person(Id) ON DELETE CASCADE
);
 
CREATE TABLE if not exists Trainer--
( 
  Id NUMERIC(3),
  ExperienceLevel NUMERIC(1) NOT NULL CHECK (ExperienceLevel IN (1, 2, 3)), 
  PRIMARY KEY (Id),
  FOREIGN KEY (Id) REFERENCES Person(Id) ON DELETE CASCADE
);

CREATE TABLE if not exists Room
(
  IdR NUMERIC(3),
  NameR VARCHAR(15) ,
  Capacity NUMERIC(3) NOT NULL,
  PRIMARY KEY (IdR)
);

CREATE TABLE if not exists Equipment
(
  IdE NUMERIC(3),
  Condition VARCHAR(1) NOT NULL CHECK (Condition IN ('T', 'F')),
  NameE VARCHAR(15),
  IdR NUMERIC(3),
  PRIMARY KEY (IdE),
  FOREIGN KEY (IdR) REFERENCES Room(IdR) ON DELETE CASCADE
);

CREATE TABLE if not exists Class
(
  IdC NUMERIC(3),
  DayInWeek VARCHAR(9) NOT NULL CHECK (dayInWeek IN ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday')), 
  Gender VARCHAR(1) NOT NULL CHECK (Gender IN ('F', 'M')),
  HourC VARCHAR(2) NOT NULL,
  IdCT NUMERIC(3),
  Id NUMERIC(3), --trainer
  IdR NUMERIC(3), 
  PRIMARY KEY (IdC),
  FOREIGN KEY (IdCT) REFERENCES ClassType(IdCT) ON DELETE CASCADE,
  FOREIGN KEY (Id) REFERENCES Trainer(Id) ON DELETE CASCADE,
  FOREIGN KEY (IdR) REFERENCES Room(IdR) ON DELETE CASCADE
);

CREATE TABLE if not exists certified_for -- מדריך מוסמך עבור סוג שיעור
(
  IdCT NUMERIC(3),
  Id NUMERIC(3),
  PRIMARY KEY (IdCT, Id),
  FOREIGN KEY (IdCT) REFERENCES ClassType(IdCT) ON DELETE CASCADE,
  FOREIGN KEY (Id) REFERENCES Trainer(Id) ON DELETE CASCADE
);

CREATE TABLE if not exists registers_for --מנוי נרשם לשיעור
(
  Id NUMERIC(3) ,
  IdC NUMERIC(3) ,
  PRIMARY KEY (Id, IdC),
  FOREIGN KEY (Id) REFERENCES Member(Id) ON DELETE CASCADE,
  FOREIGN KEY (IdC) REFERENCES Class(IdC) ON DELETE CASCADE
);
