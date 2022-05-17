CREATE PROC usp_DepositMoney (@AccountId INT, @MoneyAmount MONEY)
AS

BEGIN TRANSACTION

IF @MoneyAmount < 0
BEGIN
ROLLBACK;
THROW 50001,'Amount should be positive!', 1;
END
IF NOT EXISTS (SELECT COUNT(*) FROM Accounts WHERE  Id = @AccountId)
BEGIN
ROLLBACK;
THROW 50002, '@AccountId not found!', 1;
END
UPDATE Accounts SET Balance+= @MoneyAmount WHERE Id = @AccountId
COMMIT
GO