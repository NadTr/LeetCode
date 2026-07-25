-- Write your PostgreSQL query statement below
WITH UniqueClasses as(
    SELECT DISTINCT teacher_id, subject_id FROM Teacher
)

SELECT teacher_id, COUNT(UniqueClasses.*) as cnt
FROM UniqueCLasses
GROUP BY teacher_id