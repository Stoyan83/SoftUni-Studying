CREATE FUNCTION udf_FlightDestinationsByEmail(@email VARCHAR(50))
RETURNS INT
BEGIN
DECLARE @Destinations INT = (SELECT COUNT(*)
FROM Passengers p
JOIN FlightDestinations fd ON p.Id = fd.PassengerId
WHERE Email = @email 
GROUP BY Email)
IF @Destinations IS NULL
	RETURN 0
RETURN @Destinations
END
GO

SELECT dbo.udf_FlightDestinationsByEmail ('PierretteDunmuir@gmail.com')


SELECT dbo.udf_FlightDestinationsByEmail('Montacute@gmail.com')


SELECT dbo.udf_FlightDestinationsByEmail('MerisShale@gmail.com')
