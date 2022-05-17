CREATE TABLE NotificationEmails
(
Id INT PRIMARY KEY IDENTITY,
Recipient INT NOT NULL REFERENCES Accounts (Id),
[Subject] VARCHAR(50) NOT NULL,
Body VARCHAR(100) NOT NULL
)
GO

CREATE TRIGGER tr_EmailNotifications
ON Logs FOR INSERT
AS
BEGIN
INSERT INTO NotificationEmails(Recipient, [Subject], Body)
SELECT 
AccountId,
CONCAT('Balance change for account: ', AccountId),
CONCAT('On ', GETDATE(), ' your balance was changed from ', OldSum, ' to ', NewSum, '.')
FROM inserted
END 
