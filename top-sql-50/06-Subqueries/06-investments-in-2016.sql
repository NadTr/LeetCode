-- Write your PostgreSQL query statement below
WITH NotUniqueTiv AS(
    SELECT tiv_2015 as tiv, COUNT(*) as count FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
),
UniquePositions as (
    SELECT CONCAT(CONCAT(lat, ' - '), lon) as position, COUNT(*) as count FROM Insurance
    GROUP BY position
    HAVING COUNT(*) = 1
)

SELECT ROUND(SUM(tiv_2016)::numeric, 2) as tiv_2016 FROM Insurance
WHERE tiv_2015 IN (SELECT tiv FROM NotUniqueTiv)
AND  CONCAT(CONCAT(lat, ' - '), lon) IN (SELECT position FROM UniquePositions)
