-- Write your PostgreSQL query statement below
WITH FirstOrders AS(
    SELECT MIN(order_date) first_delivery_date, customer_id FROM Delivery
    GROUP BY customer_id
    )
SELECT 
ROUND((COUNT(*) filter(WHERE order_date = customer_pref_delivery_date) * 100.0 / COUNT(*)), 2) as immediate_percentage
FROM Delivery
JOIN FirstOrders ON Delivery.order_date = FirstOrders.first_delivery_date
    AND Delivery.customer_id = FirstOrders.customer_id