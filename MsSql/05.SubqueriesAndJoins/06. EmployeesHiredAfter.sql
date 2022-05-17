SELECT FirstName, LastName, HireDate, [Name] AS [DeptName]
FROM Employees AS e
LEFT JOIN Departments AS d ON d.DepartmentID = e.DepartmentID
WHERE DATEPART(YEAR, HireDate) > 1998 AND (d.[Name] = 'Sales' OR d.[Name] = 'Finance')
ORDER BY e.HireDate