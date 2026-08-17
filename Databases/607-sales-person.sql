-- Write your PostgreSQL query statement below
WITH REDOrders AS (
    SELECT Distinct sales_id
    FROM Orders
    JOIN COmpany ON Orders.com_id = Company.com_id
    WHERE Company.name = 'RED'
)
SELECT name FROM SalesPerson
WHERE sales_id NOT IN (SELECT sales_id FROM REDOrders)