--CREATE DATABASE Hotel

--USE Hotel

CREATE TABLE Employees
(
Id INT PRIMARY KEY IDENTITY(1,1),
FirstName VARCHAR(90) NOT NULL,
Lastname VARCHAR(90) NOT NULL,
Title VARCHAR(50) NOT NULL,
Notes VARCHAR(MAX)
)

INSERT INTO Employees (FirstName, LastName, Title, Notes) VALUES
('Gosho1', 'Goshev', 'CEO', NULL),
('Gosho2', 'Goshev', 'CEO', NULL),
('Gosho3', 'Goshev', 'CEO', NULL)

CREATE TABLE Customers
(
AccountNumber INT PRIMARY KEY,
FirstName VARCHAR(90) NOT NULL,
Lastname VARCHAR(90) NOT NULL,
PhoneNumber CHAR(10) NOT NULL,
EmergencyName VARCHAR(90),
EmergencyNumber CHAR(10)NOT NULL,
Notes VARCHAR(MAX)
)

INSERT INTO Customers (AccountNumber, FirstName, LastName, PhoneNumber, EmergencyNumber) VALUES
('1','Pesho', 'Peshov', '0886546521', '123'),
('2', 'Pesho1', 'Peshov', '0886546521', '123'),
('3', 'Pesho2', 'Peshov', '0886546521', '123')

CREATE TABLE RoomStatus
(
RoomStatus VARCHAR(30) NOT NULL,
Notes VARCHAR(MAX)
)

INSERT INTO RoomStatus (RoomStatus) VALUES
('Clean'),
('Dirty'),
('Repair')



CREATE TABLE Roomtypes
(
RoomType VARCHAR(20) NOT NULL,
Notes VARCHAR(MAX)
)


INSERT INTO RoomTypes (RoomType) VALUES
('Small'),
('Small'),
('Small')


CREATE TABLE BedTypes
(
BedType VARCHAR(20) NOT NULL,
Notes VARCHAR(MAX)
)

INSERT INTO BedTypes (BedType) VALUES
('Normal'),
('Comfort'),
('VIP')

CREATE TABLE Rooms
(
RoomNumber INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
RoomType VARCHAR(20)NOT NULL,
BedType VARCHAR(20)NOT NULL,
Rate INT,
RoomStatus VARCHAR(30),
Notes VARCHAR(MAX)
)

INSERT INTO Rooms (RoomType, BedType, RoomStatus) VALUES
('Small', 'Normal', 'clean'),
('Big', 'Normal', 'clean'),
('Small', 'Normal', 'clean')

CREATE TABLE Payments
 (
Id INT PRIMARY KEY IDENTITY(1,1) NOT NULL,
EmployeeId INT NOT NULL,
PaymentDate DATETIME NOT NULL,
AccountNumber INT NOT NULL,
FirstDateOccupied DATETIME NOT NULL,
LastDateOccupied DATETIME NOT NULL,
TotalDays INT NOT NULL,
AmountCharged Decimal(15,2),
TaxRate INT,
TaxAmount INT,
PaymentTotal Decimal(15,2),
Notes VARCHAR(MAX)
 )

 INSERT INTO Payments(EmployeeId, PaymentDate, AccountNumber, FirstDateOccupied, LastDateOccupied,TotalDays, AmountCharged, TaxRate) VALUES
(1, '2015-05-06', 7, '2015-06-18', '2015-07-03', 5, 1256.33, 166.23),
(2, '2015-05-06', 4, '2015-06-18', '2015-07-03', 6, 1256.33, 166.23),
(3, '2015-05-06', 6, '2015-06-18', '2015-07-03', 7, 1256.33, 166.23)

CREATE TABLE Occupancies 
(
Id INT PRIMARY KEY IDENTITY(1,1) NOT NULL, 
EmployeeId INT NOT NULL,
DateOccupied DATETIMe,
AccountNumber INT NOT NULL,
RoomNumber INT NOT NULL,
RateApplied INT,
PhoneCharge DECIMAL(15, 2),
Notes VARCHAR(MAX)
)

INSERT INTO Occupancies (EmployeeId, AccountNumber, RoomNumber) VALUES 
(1, 1, 1),
(2, 2, 3),
(3, 4, 5)