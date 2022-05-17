SELECT c.Id, CigarName, PriceForSingleCigar,TasteType, TasteStrength
FROM Cigars c
JOIN Tastes t ON c.TastId = t.Id
WHERE TasteType IN('Earthy', 'Woody')
ORDER BY PriceForSingleCigar DESC