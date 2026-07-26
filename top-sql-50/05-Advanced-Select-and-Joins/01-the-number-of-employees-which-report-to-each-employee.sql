-- Write your PostgreSQL query statement below
SELECT Managers.employee_id, Managers.name, 
    COUNT(Employees.employee_id) AS reports_count, 
    ROUND(AVG(Employees.age)) AS average_age
FROM Employees AS Managers
JOIN Employees ON Managers.employee_id = Employees.reports_to
GROUP BY Managers.employee_id, Managers.name

ORDER BY Managers.employee_id