-- Write your PostgreSQL query statement below
WITH FebruaryOrders AS (
    SELECT product_id, sum(unit) as total_order FROM Orders
    WHERE order_date >= TO_DATE('01/02/2020',  'DD/MM/YYYY') 
        AND order_date < TO_DATE('01/03/2020',  'DD/MM/YYYY')
    GROUP BY product_id
)
SELECT P.product_name, F.total_order as unit FROM FebruaryOrders AS F
JOIN Products as P ON F.product_id = P.product_id
WHERE F.total_order >= 100