-- Write your PostgreSQL query statement below
WITH Orders2019 AS (
    SELECT buyer_id, COUNT(*) as count 
    FROM Orders 
    WHERE date_part('year', order_date) = 2019
    GROUP BY buyer_id
)
SELECT Users.user_id as buyer_id, Users.join_date,
    COALESCE(Orders2019.count, 0) as orders_in_2019
FROM Users
LEFT JOIN Orders2019 ON Users.user_id = Orders2019.buyer_id