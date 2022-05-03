CREATE TABLE Users
(
Id BIGINT PRIMARY KEY IDENTITY(1,1),
Username  VARCHAR(30) NOT NULL,
[Password] VARCHAR(26) NOT NULL,
ProfilePicture VARCHAR(MAX),
LastLoginTime DATETIME,
IsDeleted BIT
)

INSERT INTO Users (Username, [Password], ProfilePicture, LastLoginTime, IsDeleted)
VaLUES
('SuperUser', 'Strongpass000', 'erwer', '1/01/2022', 0),
('SuperUser1', 'Strongpass000', NULL, '1/02/2021', 1),
('SuperUser2', 'Strongpass000', 'erer', '3/03/2021', 1),
('SuperUser3', 'Strongpass000', NULL, '12/15/2021', 0),
('SuperUser4', 'Strongpass000', 'rewrwer', '12/15/2021', 0)

SELECT * FROM Users
