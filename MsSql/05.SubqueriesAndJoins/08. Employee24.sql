SELECT e.EmployeeID, FirstName,
CASE 
WHEN YEAR(p.StartDate) > 2004 THEN NULL
ELSE p.[Name]
END  AS [ProjectName]
FROM Employees AS e
LEFT JOIN EmployeesProjects AS ep ON ep.EmployeeID = e.EmployeeID
LEFT JOIN Projects AS p ON p.ProjectID = ep.ProjectID
WHERE e.EmployeeID = 24