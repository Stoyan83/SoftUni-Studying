CREATE PROC usp_WithdrawMoney (@AccountId INT, @MoneyAmount MONEY)
AS

BEGIN TRANSACTION

IF (SELECT Balance FROM Accounts WHERE Id = @AccountId) < @MoneyAmount
BEGIN
ROLLBACK;
THROW 50001,'Incufficeint amount!', 1;
END
IF @MoneyAmount < 0
BEGIN
ROLLBACK;
THROW 50002,'Amount should be positive!', 1;
END
IF NOT EXISTS (SELECT COUNT(*) FROM Accounts WHERE  Id = @AccountId)
BEGIN
ROLLBACK;
THROW 50003, '@AccountId not found!', 1;
END
UPDATE Accounts SET Balance -= @MoneyAmount WHERE Id = @AccountId
COMMIT
GO