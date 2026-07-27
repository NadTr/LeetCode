-- Write your PostgreSQL query statement below
WITH UniqueEmail AS (
    SELECT MIN (id) as smallest_id, email FROM Person
    GROUP BY email
)

DELETE FROM Person WHERE id NOT IN ( SELECT smallest_id FROM UniqueEmail)