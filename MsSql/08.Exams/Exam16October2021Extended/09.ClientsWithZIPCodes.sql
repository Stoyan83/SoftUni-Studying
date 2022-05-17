SELECT FirstName + ' ' + LastName AS FullName, Country, ZIP, 
'$' + CONVERT(VARCHAR, MAX(PriceForSingleCigar)) AS CigarPrice
FROM Cigars c
JOIN ClientsCigars cc ON c.Id = cc.CigarId
JOIN Clients cl ON cc.ClientId = cl.Id
JOIN Addresses a ON cl.AddressId = a.Id
WHERE ZIP NOT LIKE '%[^0-9]%'
GROUP BY FirstName, LastName, Country, ZIP
ORDER BY FullName