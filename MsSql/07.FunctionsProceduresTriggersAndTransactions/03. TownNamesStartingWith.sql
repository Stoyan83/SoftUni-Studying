CREATE PROC usp_GetTownsStartingWith(@searchedString VARCHAR(50))
AS
BEGIN
    DECLARE @stringCount int = LEN(@searchedString)
	SELECT [Name] 
	FROM Towns
	WHERE LEFT([Name],@stringCount) = @searchedString
END

EXEC usp_GetTownsStartingWith 'b'