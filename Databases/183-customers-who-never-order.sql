-- Write your PostgreSQL query statement below
SELECT name AS Customers FROM Customers 
LEFT JOIN Orders on Customers.id = Orders.customerId
WHERE Orders.customerId IS NULL