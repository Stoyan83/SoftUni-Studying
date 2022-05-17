CREATE PROC usp_SearchByTaste(@Taste VARCHAR(30))
AS
SELECT CigarName, '$' + CONVERT(VARCHAR, PriceForSingleCigar) AS Price, TasteType,
BrandName,CONVERT(VARCHAR, [Length]) + ' ' + 'cm' AS CigarLength, CONVERT(VARCHAR, RingRange) + ' ' + 'cm' AS CigarRingRange
FROM Cigars c
JOIN Sizes s ON c.SizeId = s.Id
JOIN Brands b ON b.Id = c.BrandId
JOIN Tastes t ON t.Id = c.TastId
WHERE t.TasteType = @Taste
ORDER BY CigarLength, CigarRingRange DESC



EXEC usp_SearchByTaste 'Woody'