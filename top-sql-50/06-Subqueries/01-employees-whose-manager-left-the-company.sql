-- Write your PostgreSQL query statement below
WITH NoManager AS (
        SELECT Managers.manager_id FROM Employees AS Managers
        LEFT JOIN Employees AS Empl ON Managers.manager_id = Empl.employee_id
        WHERE Empl.employee_id IS NULL AND Managers.manager_id IS NOT NULL
)

SELECT DISTINCT Employees.employee_id FROM Employees
JOIN NoManager ON Employees.manager_id = NoManager.manager_id
WHERE Employees.salary < 30000
ORDER BY Employees.employee_id

