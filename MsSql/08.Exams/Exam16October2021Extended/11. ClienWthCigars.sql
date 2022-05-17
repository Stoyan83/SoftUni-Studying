CREATE FUNCTION udf_ClientWithCigars(@name VARCHAR(30))
RETURNS INT
AS
BEGIN
	DECLARE @Count INT = (SELECT COUNT(*) FROM Cigars AS ci
    JOIN ClientsCigars AS cc ON cc.CigarId = ci.Id
    JOIN Clients AS cl ON cl.Id = cc.ClientId
    WHERE cl.FirstName = @name )

	RETURN @Count
END




