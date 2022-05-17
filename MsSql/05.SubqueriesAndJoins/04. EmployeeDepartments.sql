SELECT TOP(5) EmployeeID, FirstName,Salary, [Name] AS [DepartmentName]
FROM Employees AS e
LEFT JOIN Departments AS d ON d.DepartmentID = e.DepartmentID
WHERE Salary > 15000
ORDER BY e.DepartmentID
