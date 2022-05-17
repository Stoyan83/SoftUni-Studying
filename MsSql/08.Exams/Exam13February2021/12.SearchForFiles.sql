CREATE PROC usp_SearchForFiles(@fileExtension VARCHAR(100))
AS
SELECT Id, Name, CONVERT(VARCHAR(100), Size) + 'KB' AS Size
FROM Files
WHERE Name LIKE '%@fileExtension'
ORDER BY Id, Name, Size


