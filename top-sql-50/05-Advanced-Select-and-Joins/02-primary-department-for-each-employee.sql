# Write your MySQL query statement below
With DepartementCount AS (
    SELECT employee_id, COUNT(department_id) as dpt_count FROM Employee 
    GROUP BY employee_id
)

SELECT Employee.employee_id, Employee.department_id FROM Employee
LEFT JOIN DepartementCount ON Employee.employee_id = DepartementCount.employee_id
WHERE Employee.primary_flag = 'Y' OR DepartementCount.dpt_count = 1