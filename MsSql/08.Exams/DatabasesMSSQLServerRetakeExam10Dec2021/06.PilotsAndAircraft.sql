SELECT FirstName, LastName, Manufacturer, Model, FlightHours
FROM Pilots p
JOIN PilotsAircraft pa ON p.Id = pa.PilotId
JOIN Aircraft a ON pa.AircraftId = a.Id
WHERE FlightHours IS NOT NULL AND FlightHours <= 304
ORDER BY FlightHours DESC, FirstName