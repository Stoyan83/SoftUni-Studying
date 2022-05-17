SELECT p.FullName, COUNT(*) AS CountOfAircraft, SUM(TicketPrice) AS TotalPayed
FROM Aircraft a
JOIN FlightDestinations fd ON a.Id = fd.AircraftId
JOIN Passengers p ON fd.PassengerId = p.Id
GROUP BY p.FullName
HAVING COUNT(*) > 1 AND FullName LIKE '_a%'
ORDER BY FullName