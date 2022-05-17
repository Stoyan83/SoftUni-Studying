CREATE PROC usp_GetHoldersWithBalanceHigherThan(@Balance DECIMAL(18,4))
AS
BEGIN
SELECT FirstName AS [First Name], LastName as [Last Name]
FROM AccountHolders ah
JOIN Accounts a ON a.AccountHolderId = ah.Id
GROUP BY FirstName, LastName
HAVING SUM(Balance) > @Balance
ORDER BY FirstName, LastName
END
 
