CREATE PROC usp_GetHoldersFullName
AS
BEGIN
SELECT FirstName + ' ' + LastName as [Full Name]
FROM AccountHolders
END

EXEC usp_GetHoldersFullName