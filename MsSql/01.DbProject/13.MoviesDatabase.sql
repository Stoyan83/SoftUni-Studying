CREATE DATABASE Movies

CREATE TABLE Directors
(
Id INT PRIMARY KEY IDENTITY(1,1),
DirectorName VARCHAR(30) NOT NULL,
Notes VARCHAR(MAX)
)

INSERT INTO Directors (DirectorName) VALUES
('Speilberg'),
('Tarantino'),
('Tarantino'),
('Tarantino'),
('Tarantino')

CREATE TABLE Genres
(
Id INT PRIMARY KEY IDENTITY(1,1),
GenreName VARCHAR(30) NOT NULL,
Notes VARCHAR(MAX)
)

INSERT INTO Genres (GenreName) VALUES
('action'),
('action'),
('action'),
('action'),
('action')

CREATE TABLE Categories 
(
Id INT PRIMARY KEY IDENTITY(1,1),
CategoryName VARCHAR(30) NOT NULL,
Notes VARCHAR(MAX)
)

INSERT INTO Categories  (CategoryName) VALUES
('action'),
('action'),
('action'),
('action'),
('action')

CREATE TABLE Movies
(
Id INT PRIMARY KEY IDENTITY(1,1),
Title VARCHAR(30) NOT NULL,
DirectorId Int  NOT NULL,
CopyrightYear DATE,
[Length] INT,
GenreId INT,
CategoryId INT,
Notes VARCHAR(MAX)
)

INSERT INTO Movies (Title, DirectorId) VALUES
('Boom', '1'),
('Boom', '1'),
('Boom', '1'),
('Boom', '1'),
('Boom', '1')