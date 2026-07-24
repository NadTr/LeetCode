-- Write your PostgreSQL query statement below
WITH Managers AS (
    SELECT managerId, COUNT(*) AS reports FROM Employee
    GROUP BY managerId
)
SELECT Employee.name FROM Employee
JOIN Managers ON Employee.id = Managers.managerId
WHERE Managers.reports >= 5