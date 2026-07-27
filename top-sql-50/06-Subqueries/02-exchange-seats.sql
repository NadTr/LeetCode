-- -- Write your PostgreSQL query statement below
WITH MaxId AS (
    SELECT MAX(id) as max FROM Seat
)

SELECT 
    CASE 
        WHEN id = (SELECT max from MaxId) AND id % 2 =1 THEN id 
        WHEN id % 2 = 0 THEN (id -1) 
        ELSE (id + 1) 
    END AS id 
    , student
FROM Seat
ORDER BY id