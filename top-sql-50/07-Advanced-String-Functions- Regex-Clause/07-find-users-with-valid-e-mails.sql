-- Write your PostgreSQL query statement below
SELECT * FROM Users
WHERE mail ~ '^[a-zA-Z0-9_.-]+@leetcode\.com$'
AND LEFT(mail, 1) ~* '[a-z]'