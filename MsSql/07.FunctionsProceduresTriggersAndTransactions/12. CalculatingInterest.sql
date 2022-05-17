CREATE FUNCTION ufn_CalculateFutureValue
(@Sum DECIMAL(18,4),  @YearlyInterest float, @NumberOfYears INT)
RETURNS DECIMAL(18,4)
AS
BEGIN
DECLARE @FutureValue DECIMAL(18,4)
SET @FutureValue = @Sum * (POWER(1 + @YearlyInterest, @NumberOfYears))
RETURN @FutureValue
END

GO

CREATE PROC usp_CalculateFutureValueForAccount(@AccountId INT, @InterestRate FLOAT)
AS
BEGIN
SELECT a.Id, FirstName, LastName, Balance, 
dbo.ufn_CalculateFutureValue(a.Balance,@InterestRate, 5) AS [Balance in 5 years]
FROM AccountHolders ah
JOIN Accounts a ON a.AccountHolderId = ah.Id
WHERE a.Id = @AccountId 
END

GO  
