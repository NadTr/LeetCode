-- Write your PostgreSQL query statement below
WITH RootNode AS (
    SELECT id FROM Tree WHERE p_id IS null
),
LeafNode AS(
    SELECT id FROM Tree 
    WHERE id NOT IN (SELECT Distinct p_id FROM Tree WHERE p_id IS NOT NULL)
        AND id not in (SELECT id FROM RootNode) 
)

SELECT id, 'Root' as type FROM RootNode
UNION
SELECT id, 'Inner' as type FROM Tree
WHERE id not in (SELECT id FROM RootNode) 
    AND id not in (SELECT id FROM LeafNode)
UNION
SELECT id, 'Leaf' as type FROM LeafNode