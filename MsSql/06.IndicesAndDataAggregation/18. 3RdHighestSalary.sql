SELECT DepartmentID, Salary FROM
(SELECT DepartmentID, Salary,
DENSE_RANK() OVER(PARTITION BY DepartmentID ORDER BY Salary DESC) AS SalaryRank
FROM Employees
GROUP BY DepartmentID, Salary) AS s
WHERE SalaryRank = 3


--SELECT DISTINCT DepartmentID, Salary FROM
--(SELECT DepartmentID, Salary,
--DENSE_RANK() OVER(PARTITION BY DepartmentID ORDER BY Salary DESC) AS SalaryRank
--FROM Employees) AS s
--WHERE SalaryRank = 3
