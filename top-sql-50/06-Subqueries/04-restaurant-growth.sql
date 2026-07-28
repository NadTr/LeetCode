-- Write your PostgreSQL query statement below
WITH AmountByDay AS(
    SELECT visited_on, SUM(amount) as amount FROM Customer
    GROUP BY visited_on
)
SELECT DISTINCT C.visited_on, 
    ROUND((SELECT SUM(amount) FROM AmountByDay C1 where C1.visited_on BETWEEN C.visited_on - INTERVAL '6 day' AND C.visited_on), 2) as amount, 
    ROUND((SELECT AVG(amount) FROM AmountByDay C1 where C1.visited_on BETWEEN C.visited_on - INTERVAL '6 day' AND C.visited_on), 2) as average_amount 
FROM AmountByDay C
ORDER BY C.visited_on ASC
OFFSET 6