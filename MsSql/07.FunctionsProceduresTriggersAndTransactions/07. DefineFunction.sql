CREATE FUNCTION ufn_IsWordComprised
(@SetOfLetters VARCHAR(MAX), @Word VARCHAR(MAX))
RETURNS INT
AS 
BEGIN
	DECLARE @Count INT = 1
	WHILE (@Count <= LEN(@Word))
		BEGIN 
			IF CHARINDEX(SUBSTRING(@Word, @Count, 1), @SetOfLetters ) = 0
				Return 0

			SET @Count += 1
		END
		RETURN 1
END
GO
