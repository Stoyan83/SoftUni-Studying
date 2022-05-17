SELECT  ap.AirportName, fd.[Start] AS DayTime, TicketPrice, p.FullName, a.Manufacturer, a.Model
FROM Aircraft a
JOIN FlightDestinations fd ON a.Id = fd.AircraftId
JOIN Airports ap ON fd.AirportId = ap.Id
JOIN Passengers p ON fd.PassengerId = p.Id
WHERE DATEPART(HOUR, fd.[Start]) BETWEEN 6 AND 20 AND TicketPrice > 2500
ORDER BY Model