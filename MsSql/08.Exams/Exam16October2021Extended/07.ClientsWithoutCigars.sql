SELECT c.Id, FirstName + ' ' + LastName AS ClientName, Email
FROM Clients c
WHERE c.Id NOT IN (SELECT ClientId FROM ClientsCigars)
ORDER BY ClientName
 

