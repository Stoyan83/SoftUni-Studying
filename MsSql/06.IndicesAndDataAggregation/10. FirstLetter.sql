SELECT Left(FirstName, 1) AS FirstLetter
FROM WizzardDeposits
WHERE DepositGroup = 'Troll Chest'
GROUP BY Left(FirstName, 1)
ORDER BY Left(FirstName, 1)