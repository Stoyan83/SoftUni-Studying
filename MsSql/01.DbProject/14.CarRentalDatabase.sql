CREATE DATABASE CarRental
GO

CREATE TABLE Categories
(
ID INT PRIMARY KEY IDENTITY(1, 1),
CategoryName VARCHAR(30) NOT NULL,
DailyRate REAL,
WeeklyRate REAL,
MonthlyRate REAL,
WeekendRate REAL
)

INSERT INTO Categories(CategoryName) 
VALUES ('Car'),
	   ('Byke'),
	   ('BUS')


CREATE TABLE Cars (
Id INT PRIMARY KEY IDENTITY(1, 1),
PlateNumber VARCHAR(10),
Manufacturer VARCHAR(20),
Model VARCHAR(20) NOT NULL,
CarYear INT ,
CategoryId INT,
Doors INT,
Picture VARBINARY(MAX),
Condition NVARCHAR(MAX),
Available BIT,
)

INSERT INTO Cars(Model)
VALUES('Suzuki'),
	  ('Suzuki'),
	  ('Suzuki')

CREATE TABLE Employees (
    Id INT PRIMARY KEY IDENTITY(1, 1),
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50),
    Title VARCHAR(50),
    Notes VARCHAR(MAX)
)

INSERT INTO Employees(FirstName)
VALUES('Gosho'),
      ('Pesho'),
      ('Ivan')

CREATE TABLE Customers (
    Id INT PRIMARY KEY IDENTITY(1, 1),
    DriverLicenseNumber INT NOT NULL,
    FullName NVARCHAR(100),
    Adress NVARCHAR(100),
    City NVARCHAR(50),
    ZIPCode INT,
    Notes NVARCHAR(MAX)
)

INSERT INTO Customers(DriverLicenseNumber)
VALUES(55555),
      (55545),
      (55355)

CREATE TABLE RentalOrders (
    Id INT PRIMARY KEY IDENTITY(1, 1),
    EmployeeId INT NOT NULL,
    CustomerId INT,
    CarId INT,
    TankLevel INT,
    KilometrageStart INT,
    KilometrageEnd INT,
	TotalKilometrage INT,
    StartDate DATE,
    EndDate DATE ,
    TotalDays REAL,
    TaxRate REAL,
    OrderStatus VARCHAR(50),
    Notes VARCHAR(MAX)
)

INSERT INTO RentalOrders(EmployeeId)
VALUES(1234),
      (654641),
      (54654)