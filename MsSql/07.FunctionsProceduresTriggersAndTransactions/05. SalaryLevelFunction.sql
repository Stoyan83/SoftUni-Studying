CREATE FUNCTION ufn_GetSalaryLevel(@salary DECIMAL(18,4))
RETURNS varchar(7)
AS 
BEGIN 
	DECLARE @SalaryLevel VARCHAR(7)
	IF @salary < 30000
		SET @SalaryLevel= 'Low'
	ELSE IF @salary BETWEEN 30000 AND 50000
		SET @SalaryLevel='Average'
	ELSE
		SET @SalaryLevel= 'High'
	RETURN @SalaryLevel
END
GO

--CREATE FUNCTION ufn_GetSalaryLevel(@salary DECIMAL(18,4))
--RETURNS varchar(7)
--AS 
--BEGIN 
--	IF @salary < 30000
--		RETURN 'Low'
--	ELSE IF @salary BETWEEN 30000 AND 50000
--		RETURN 'Average'	
--	RETURN 'High'
--END
--GO


SELECT Salary,
dbo.ufn_GetSalaryLevel(Salary) AS [Salary Level]
FROM Employees
