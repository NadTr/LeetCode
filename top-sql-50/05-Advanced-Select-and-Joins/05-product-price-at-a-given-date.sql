-- Write your PostgreSQL query statement below
WITH LastChange AS(
    SELECT product_id, MAX(change_date) AS last_date_before FROM Products
    WHERE change_date  <= TO_DATE('2019-08-16', 'YYYY-MM-DD')
    GROUP BY product_id
)

SELECT DISTINCT Products.product_id, CASE WHEN last_date_before IS NULL THEN 10 ELSE Products.new_price END AS price FROM Products
LEFT JOIN LastChange ON Products.product_id = LastChange.product_id
WHERE Products.change_date = LastChange.last_date_before
    OR last_date_before IS NULL