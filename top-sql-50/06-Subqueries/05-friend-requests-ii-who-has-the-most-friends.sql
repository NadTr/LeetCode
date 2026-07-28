-- Write your PostgreSQL query statement below
WITH Friendship AS (
    SELECT requester_id as friend1, accepter_id as friend2 FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as friend1, requester_id as friend2 FROM RequestAccepted
),
MostFriends AS (
    SELECT friend1 as id, COUNT(friend2) as num FROM Friendship
    GROUP BY friend1
)

SELECT id,  num FROM MostFriends
ORDER BY num DESC
LIMIT 1
