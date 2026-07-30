-- Write your PostgreSQL query statement below
With Ranks as (
    SELECT score, ROW_NUMBER() OVER (ORDER BY score DESC) AS rank
    FROM (SELECT DISTINCT score FROM Scores)
)
SELECT Scores.score,
    Ranks.rank 
FROM Scores
JOIN Ranks ON Scores.score = Ranks.score
ORDER BY score desc