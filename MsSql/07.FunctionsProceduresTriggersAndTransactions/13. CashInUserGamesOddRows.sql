Create FUNCTION ufn_CashInUsersGames (@GameName VARCHAR(50))
RETURNS TABLE 
AS 
RETURN SELECT SUM(Cash) AS [SumCash]
FROM

(SELECT g.Name, ug.Cash,
ROW_NUMBER() OVER(ORDER BY ug.Cash DESC) AS RowNum
FROM Games g
JOIN UsersGames ug ON g.Id = ug.GameId
WHERE g.Name = @GameName) AS ?
WHERE ?.RowNum % 2 != 0

GO

SELECT *
FROM dbo.ufn_CashInUsersGames('Love in a mist')
