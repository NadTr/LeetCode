-- Write your PostgreSQL query statement below
SELECT user_id, 
    CONCAT(upper(SUBSTRING(name FROM 1 FOR 1)), lower(SUBSTRING(name FROM 2))) as name 
FROM Users
ORDER BY user_id