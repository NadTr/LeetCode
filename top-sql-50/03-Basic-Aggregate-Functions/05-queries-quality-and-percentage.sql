-- Write your PostgreSQL query statement below
SELECT query_name, 
    ROUND( AVG(rating::numeric / position) ,2) as quality,
    ROUND(COUNT(CASE WHEN rating < 3 THEN 1 ELSE null END) *100.0 / COUNT(*) ,2) as poor_query_percentage
FROM Queries

GROUP BY query_name