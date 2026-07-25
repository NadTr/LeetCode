-- Write your PostgreSQL query statement below
SELECT project_id,
ROUND(AVG(experience_years *1.0), 2) as average_years

FROM Project
JOIN Employee ON Project.employee_id = Employee.employee_id
GROUP BY project_id