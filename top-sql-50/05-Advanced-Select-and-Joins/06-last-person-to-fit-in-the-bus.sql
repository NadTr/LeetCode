-- Write your PostgreSQL query statement below
WITH WeightByTurn AS( 
    SELECT turn, 
        (SELECT sum(weight) FROM Queue Q1 WHERE  Q1.turn <= Q.turn) as weight_by_turn 
    FROM Queue Q
    ORDER BY turn
),
LastTurn AS(
    SELECT MAX(turn) as last_turn FROM WeightByTurn
    WHERE weight_by_turn <= 1000
)
SELECT person_name FROM Queue
JOIN LastTurn ON Queue.turn = LastTurn.last_turn