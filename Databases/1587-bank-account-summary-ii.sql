-- Write your PostgreSQL query statement below
SELECT U.name, SUM(T.amount) as balance FROM Users U
JOIN Transactions T ON U.account = T.account
GROUP BY U.name, U.account
HAVING SUM(T.amount) > 10000