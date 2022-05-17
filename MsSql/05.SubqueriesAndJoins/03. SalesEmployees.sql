SELECT TOP(50) EmployeeID, FirstName, LastName, [Name]
FROM Employees AS e
LEFT JOIN Departments AS d ON d.DepartmentID = e.DepartmentID
WHERE [Name] = 'Sales'