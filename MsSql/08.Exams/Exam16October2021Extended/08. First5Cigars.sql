SELECT TOP 5 CigarName, PriceForSingleCigar, ImageURL 
FROM Cigars c
JOIN Sizes s ON c.SizeId = s.Id
WHERE [Length] >=  12 AND (CigarName LIKE '%ci%' OR PriceForSingleCigar > 50)
AND RingRange > 2.55
ORDER BY CigarName, PriceForSingleCigar DESC
