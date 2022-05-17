--CREATE DATABASE CigarShop
--USE CigarShop

CREATE TABLE Sizes
(
Id INT PRIMARY KEY IDENTITY,
[Length] INT NOT NULL,
CHECK([Length] BETWEEN 10 AND 25),
RingRange DECIMAL(18,2) NOT NULL,
CHECK(RingRange BETWEEN 1.5 AND 7.5)
)

CREATE TABLE Tastes
(
Id INT PRIMARY KEY IDENTITY,
TasteType VARCHAR(20) NOT NULL,
TasteStrength VARCHAR(15) NOT NULL,
ImageURL NVARCHAR(100) NOT NULL
)

CREATE TABLE Brands
(
Id INT PRIMARY KEY IDENTITY,
BrandName VARCHAR(30) NOT NULL UNIQUE,
BrandDescription VARCHAR(MAX)
)

CREATE TABLE Cigars
(
Id INT PRIMARY KEY IDENTITY,
CigarName VARCHAR(80) NOT NULL,
BrandId INT NOT NULL REFERENCES Brands(Id),
TastId INT NULL REFERENCES Tastes(Id),
SizeId INT NOT NULL REFERENCES Sizes(Id),
PriceForSingleCigar MONEY NOT NULL,
ImageURL NVARCHAR(100) NOT NULL
)

CREATE TABLE Addresses
(
Id INT PRIMARY KEY IDENTITY,
Town VARCHAR(30) NOT NULL,
Country NVARCHAR(30) NOT NULL,
Streat NVARCHAR(100) NOT NULL,
ZIP VARCHAR(20) NOT NULL
)

CREATE TABLE Clients
(
Id INT PRIMARY KEY IDENTITY,
FirstName NVARCHAR(30) NOT NULL,
LastName NVARCHAR(30) NOT NULL,
Email NVARCHAR(50) NOT NULL,
AddressId INT NOT NULL REFERENCES Addresses(Id)
)

CREATE TABLE ClientsCigars
(
ClientId INT  NOT NULL REFERENCES Clients(Id),
CigarId INT  NOT NULL REFERENCES Cigars(Id),
PRIMARY KEY(ClientId, CigarId) 
)