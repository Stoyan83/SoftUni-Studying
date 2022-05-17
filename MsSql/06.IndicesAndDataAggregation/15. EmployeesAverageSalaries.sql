--SELECT DepartmentID, AVG(NewSalary) AS AverageSalary
-- FROM
--(SELECT FirstName,DepartmentID, Salary,
--CASE 
--WHEN DepartmentID = 1 THEN Salary + 5000
--ELSE Salary
--END AS NewSalary 
--FROM Employees
--WHERE Salary > 30000 AND ManagerID != 42) AS s
--GROUP BY DepartmentID

SELECT * INTO NewEmployeeTableDB
	FROM Employees
	WHERE Salary > 30000

DELETE 
	FROM NewEmployeeTableDB
	WHERE ManagerID = 42

UPDATE NewEmployeeTableDB
	SET Salary += 5000
	WHERE DepartmentID = 1

SELECT DepartmentID, 
	AVG(Salary) AS [AverageSalary]
	FROM NewEmployeeTableDB
	GROUP BY DepartmentID