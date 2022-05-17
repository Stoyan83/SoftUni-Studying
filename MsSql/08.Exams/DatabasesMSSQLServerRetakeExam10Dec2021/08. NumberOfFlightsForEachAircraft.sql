SELECT  a.Id,a.Manufacturer, a.FlightHours, 
COUNT(*) AS FlightDestinationsCount, ROUND(Avg(TicketPrice), 2) AS AvgPrice
FROM Aircraft a
JOIN FlightDestinations fd ON a.Id = fd.AircraftId
GROUP BY a.Id, a.Manufacturer,a.FlightHours, a.Model
HAVING COUNT(*) >= 2
ORDER BY COUNT(*) DESC, a.Id

