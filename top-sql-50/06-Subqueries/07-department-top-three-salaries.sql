-- Write your PostgreSQL query statement below
WITH TopSalaries as (
    SELECT departmentId, (SELECT DISTINCT salary FROM Employee As E 
        WHERE E.departmentId = Emp.departmentId 
        ORDER BY salary DESC LIMIT 1 OFFSET 2) as top3
    FROM Employee as Emp
    GROUP BY departmentId
)

SELECT Department.name as Department, Employee.name as Employee, Employee.salary as Salary
FROM Employee
LEFT JOIN TopSalaries ON Employee.departmentId = TopSalaries.departmentId
JOIN Department ON Employee.departmentId = Department.id
    AND Employee.salary >= COALESCE(TopSalaries.top3, 0)
