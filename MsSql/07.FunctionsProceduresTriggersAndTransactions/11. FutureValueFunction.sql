CREATE FUNCTION ufn_CalculateFutureValue
(@Sum DECIMAL(18,4),  @YearlyInterest FLOAT, @NumberOfYears INT)
RETURNS DECIMAL(18,4)
AS
BEGIN
DECLARE @FutureValue DECIMAL(18,4)
SET @FutureValue = @Sum * (POWER((1 + @YearlyInterest), @NumberOfYears))
RETURN @FutureValue
END

GO

SELECT dbo.ufn_CalculateFutureValue(1000, 0.1, 5)

