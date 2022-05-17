UPDATE Cigars 
SET PriceForSingleCigar *= 1.2
FROM Cigars c
JOIN Tastes t ON c.TastId = t.Id
WHERE TasteType = 'Spicy'
UPDATE Brands
SET BrandDescription = 'New description'
WHERE BrandDescription is NULL

