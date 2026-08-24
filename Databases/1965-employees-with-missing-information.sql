-- Write your PostgreSQL query statement below
SELECT coalesce(E.employee_id, S.employee_id) as employee_id FROM Employees E
FULL JOIN Salaries S ON E.employee_id = S.employee_id
WHERE E.name IS NULL OR S. salary IS NULL
ORDER BY 1 ASC
