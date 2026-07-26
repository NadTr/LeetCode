-- Write your PostgreSQL query statement below
WITH UniqueNumber AS (
    SELECT num, COUNT(*) AS count FROM MyNumbers
    GROUP BY num
)
SELECT max(num) as num FROM UniqueNumber
WHERE count = 1