-- Write your PostgreSQL query statement below
WITH LotOfPeople AS(
    SELECT * FROM Stadium
    WHERE people >= 100
    ORDER BY id
)
SELECT * FROM LotOfPeople
WHERE (id-2 IN (SELECT id FROM LotOfPeople) AND id-1 IN (SELECT id FROM LotOfPeople)) 
    OR (id-1 IN (SELECT id FROM LotOfPeople)AND id+1 IN (SELECT id FROM LotOfPeople)) 
    OR (id+1 IN (SELECT id FROM LotOfPeople) AND id+2 IN (SELECT id FROM LotOfPeople))
ORDER BY visit_date