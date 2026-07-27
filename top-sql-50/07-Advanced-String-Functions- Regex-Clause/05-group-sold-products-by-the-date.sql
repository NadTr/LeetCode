-- Write your PostgreSQL query statement below 
WITH OrderedActivities AS (
    SELECT DISTINCT * FROM Activities
    ORDER BY sell_date, product
)
SELECT DISTINCT sell_date , COUNT(product) as num_sold,
    string_agg(product, ',') as products
FROM OrderedActivities
GROUP BY sell_date
ORDER BY sell_date
