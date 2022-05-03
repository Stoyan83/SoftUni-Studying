BACKUP DATABASE SoftUni TO DISK='/var/opt/mssql/data/Minions.bak'

DROP DATABASE SoftUni

RESTORE DATABASE SoftUni FROM DISK='/var/opt/mssql/data/Minions.bak'