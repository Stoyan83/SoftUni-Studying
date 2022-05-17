CREATE PROC usp_GetEmployeesFromTown (@TownName VARCHAR(50))
AS 
BEGIN 
	SELECT FirstName, LastName
	FROM Employees e
	JOIN Addresses a ON a.AddressID = e.AddressID
	JOIN Towns t ON t.TownID = a.TownID
	WHERE t.Name = @TownName
END


EXEC usp_GetEmployeesFromTown 'Sofia'

