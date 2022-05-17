SELECT TOP 20 fd.Id, [Start], FullName, AirportName, TicketPrice
FROM Passengers p
JOIN FlightDestinations fd ON p.Id = fd.PassengerId
JOIN Airports a ON fd.AirportId = a.Id
WHERE CONVERT(INT, DAY([Start])) % 2 = 0
ORDER BY TicketPrice DESC