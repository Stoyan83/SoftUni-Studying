CREATE TABLE Logs
(
LogId INT PRIMARY KEY IDENTITY ,
AccountId INT REFERENCES Accounts(Id) NOT NULL,
OldSum MONEY,
NewSum MONEY
)
GO 

CREATE TRIGGER tr_Logs
ON Accounts FOR UPDATE
AS 
BEGIN
INSERT INTO Logs(AccountId, OldSum, NewSum)
Select i.AccountHolderId, d.Balance, i.Balance
FROM inserted i
JOIN deleted d ON d.Id=i.Id
END