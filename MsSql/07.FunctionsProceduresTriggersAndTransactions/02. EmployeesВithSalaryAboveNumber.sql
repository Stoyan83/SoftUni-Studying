CREATE PROC usp_GetEmployeesSalaryAboveNumber
(@Amount decimal(18,4))
AS
BEGIN
SELECT FirstName, LastName
FROM Employees
WHERE Salary >= @Amount
END


EXEC usp_GetEmployeesSalaryAboveNumber @Amount = 48100