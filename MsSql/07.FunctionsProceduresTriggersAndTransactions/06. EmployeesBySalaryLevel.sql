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


CREATE PROC usp_EmployeesBySalaryLevel(@SalaryLevel VARCHAR(7))
AS
BEGIN
	SELECT FirstName AS [First Name], 
	LastName AS [Last Name]
	FROM Employees
	WHERE @SalaryLevel = dbo.ufn_GetSalaryLevel(Salary)
END

EXEC usp_EmployeesBySalaryLevel 'High'