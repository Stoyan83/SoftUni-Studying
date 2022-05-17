CREATE PROC usp_DeleteEmployeesFromDepartment (@departmentId INT)
AS
BEGIN

ALTER TABLE Departments
ALTER COLUMN ManagerID int NULL

DELETE
FROM EmployeesProjects
WHERE EmployeeID IN 
(SELECT EmployeeID FROM Employees WHERE DepartmentID = @departmentId)

UPDATE Employees
SET ManagerID=NULL
WHERE ManagerID IN
(SELECT EmployeeID FROM Employees WHERE DepartmentID = @departmentId)

UPDATE Departments
SET ManagerID = NULL
WHERE ManagerID IN 
(SELECT EmployeeID FROM Employees WHERE DepartmentID = @departmentId)

DELETE FROM Employees
WHERE DepartmentID=@departmentId

DELETE FROM Departments
where DepartmentID=@departmentId

SELECT count(*)
FROM Employees
where DepartmentID=@departmentId

END