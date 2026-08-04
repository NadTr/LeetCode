-- Write your PostgreSQL query statement below
WITH FirstLastScore AS (
    SELECT student_id, subject, 
        FIRST_VALUE(score) OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date ASC
            ) as first_score,
        FIRST_VALUE(score) OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date DESC
            ) as latest_score
    FROM Scores
)

SELECT DISTINCT student_id, subject, first_score, latest_score 
FROM FirstLastScore
WHERE latest_score > first_score
ORDER BY student_id, subject