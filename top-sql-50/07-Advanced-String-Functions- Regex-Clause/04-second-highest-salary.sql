-- Write your PostgreSQL query statement below
WITH SecondHighest AS (
    SELECT DISTINCT salary FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
)
SELECT max(salary) as SecondHighestSalary 
FROM SecondHighest