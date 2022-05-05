CREATE DATABASE Minions

--Minions (Id, Name, Age). Then add new table Towns (Id, Name).

CREATE TABLE Minions
(
	Id INT PRIMARY KEY, 
	[Name] VARCHAR(30),
	Age INT,
)

CREATE TABLE Towns
(
Id INT PRIMARY KEY,
[Name] VARCHAR(50),
) 

ALTER TABLE Minions 
ADD TownId INT

ALTER TABLE Minions
ADD FOREIGN KEY (TownId) REFERENCES Towns(Id)

DELETE From Minions

DROP TABLE Minions
DROP TABLE Towns
