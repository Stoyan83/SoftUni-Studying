CREATE TABLE People
(
Id INT PRIMARY KEY IDENTITY(1,1),
[Name] NVARCHAR(200) NOT NULL,
Picture VARBINARY(MAX),
Height DECIMAL(15, 2),
[Weight] DECIMAL(15, 2),
Gender CHAR(1) NOT NULL,
Birthdate DATE NOT NULL,
Biography  NVARCHAR(MAX)
)


INSERT INTO People (Name, Height, Weight, Gender, Birthdate) VALUES 
('Ivan', 1.7999999, 1.7999999, 'm', '01/15/1999'),
('Georgi',1.7999999, 1.7999999, 'm', '01/15/1999'),
('Peter',  1.7999999 ,1.7999999, 'm', '01/15/1999'),
('Joro',  1.7999999, 1.7999999, 'm', '01/15/1999'),
('Vankata', 1.79999999, 1.7999999, 'm', '01/15/1999')