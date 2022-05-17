SELECT LastName, AVG(s.[Length]) AS CiagrLength, CEILING(AVG(s.RingRange))
FROM Clients c
JOIN ClientsCigars cc ON c.Id = cc.ClientId
JOIN Cigars cg ON cc.CigarId = cg.Id
JOIN Sizes s ON cg.SizeId = s.Id
GROUP BY LastName
ORDER BY CiagrLength DESC


