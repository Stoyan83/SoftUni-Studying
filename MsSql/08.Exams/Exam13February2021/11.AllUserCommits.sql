CREATE FUNCTION udf_AllUserCommits(@username VARCHAR(30))
RETURNS INT
AS
BEGIN
IF NOT EXISTS(SELECT 1 FROM Users WHERE Username = @username)
	RETURN 0
	DECLARE @Count INT =  (SELECT ISNULL(COUNT(c.Id), 0) FROM Users AS u
		LEFT JOIN Commits AS c ON c.ContributorId  = u.Id
		WHERE u.Username = @username
		GROUP BY u.Id);

	RETURN @Count
END

SELECT dbo.udf_AllUserCommits('dfsdfasd')