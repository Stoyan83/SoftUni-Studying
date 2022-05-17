SELECT ContinentCode, CurrencyCode, CurrancyUsage 
FROM(SELECT c.ContinentCode, c.CurrencyCode,
COUNT(c.CurrencyCode) AS [CurrancyUsage],
DENSE_RANK() OVER(PARTITION BY ContinentCode ORDER BY COUNT(c.CurrencyCode) DESC) AS Ranked
FROM Countries AS c
GROUP BY c.ContinentCode, c.CurrencyCode
) AS c
WHERE Ranked = 1 AND CurrancyUsage > 1
ORDER BY ContinentCode