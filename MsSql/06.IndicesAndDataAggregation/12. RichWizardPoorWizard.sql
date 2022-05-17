 SELECT SUM([Difference]) FROM
 (SELECT 
(DepositAmount - LEAD(DepositAmount,1) OVER (ORDER BY id)) AS [Difference]
FROM WizzardDeposits) AS c


--SELECT SUM([Difference]) FROM(
--SELECT FirstName AS HostWirzard,
--DepositAmount AS HostWizardDeposit,
--LEAD(FirstName) OVER (ORDER BY Id ) AS GuestWizard,
--LEAD(DepositAmount) OVER (ORDER BY id) AS GuestDeposit,
--(DepositAmount - LEAD(DepositAmount) OVER (ORDER BY id)) AS [Difference]
--FROM WizzardDeposits) AS c
