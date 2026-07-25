-- Write your PostgreSQL query statement below
SELECT contest_id,
     ROUND((COUNT(Register.user_id) ::numeric / (SELECT DISTINCT COUNT(*) FROM Users)) * 100 , 2) AS percentage
FROM Register
GROUP BY contest_id
Order BY percentage DESC, contest_id ASC