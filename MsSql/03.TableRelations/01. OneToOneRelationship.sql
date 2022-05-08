CREATE TABLE Passports
(
PassportId INT PRIMARY KEY IDENTITY(101,1),
PassportNumber CHAR(8)
)


CREATE TABLE Persons
(
PersonId INT PRIMARY KEY IDENTITY,
FirstName VARCHAR(30),
Salary MONEY,
PassportId INT UNIQUE FOREIGN KEY REFERENCES Passports(PassportId)
)

INSERT INTO Passports(PassportNumber)
VALUES('N34FG21B'),
      ('K65LO4R7'),
      ('ZE657QP2')

INSERT INTO Persons (FirstName, Salary, PassportId)
VALUES ('Roberto',43300.00, 102),
        ('Tom', 56100.00, 103),
		('Yana', 60200.00, 101)