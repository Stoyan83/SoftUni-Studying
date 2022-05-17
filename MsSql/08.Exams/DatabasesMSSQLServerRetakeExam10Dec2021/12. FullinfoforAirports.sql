CREATE PROC usp_SearchByAirportName(@airportName VARCHAR(70))
AS
BEGIN
SELECT AirportName, FullName, 
CASE
WHEN TicketPrice <= 400 THEN 'Low'
WHEN TicketPrice BETWEEN 401 AND 1500 THEN 'Medium'
ELSE 'High'
END AS LevelOfTickerPrice, 
Manufacturer, Condition, TypeName
FROM Airports a
JOIN FlightDestinations fd ON a.Id = fd.AirportId
JOIN Passengers p ON fd.PassengerId = p.Id
JOIN Aircraft ac ON fd.AircraftId = ac.Id
JOIN AircraftTypes a2 ON ac.TypeId = a2.Id
WHERE AirportName = @airportName
ORDER BY Manufacturer, FullName
END


