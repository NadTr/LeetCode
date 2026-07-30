-- Write your PostgreSQL query statement below
WITH UnbannedDrives as (
    SELECT * FROM Trips
    JOIN Users as Clients ON Trips.client_id = Clients.users_id
        AND Clients.banned = 'No'
    JOIN Users as Drivers ON Trips.driver_id = Drivers.users_id
        AND Drivers.banned = 'No'
    WHERE TO_DATE(request_at, 'YYY-MM-DD') BETWEEN TO_DATE('2013-10-01', 'YYYY-MM-DD') AND TO_DATE('2013-10-03', 'YYYY-MM-DD')
)

SELECT request_at AS Day,
    ROUND(COUNT(case when status in ('cancelled_by_driver', 'cancelled_by_client') then 1 else null end)::numeric / count(*), 2) AS "Cancellation Rate"
FROM UnbannedDrives
GROUP BY request_at
