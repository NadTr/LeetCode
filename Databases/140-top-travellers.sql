-- Write your PostgreSQL query statement below
WITH Travel AS(
    SELECT user_id, SUM(Rides.distance) as travelled_distance 
    FROM Rides
    GROUP BY user_id
)

SELECT Users.name, COALESCE(Travel.travelled_distance, 0) as travelled_distance 
FROM Users
LEFT JOIN Travel ON Users.id = Travel.user_id 
ORDER BY 2 DESC, 1 ASC