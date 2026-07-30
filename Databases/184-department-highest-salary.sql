-- Write your PostgreSQL query statement below
WITH DepartmentHighest AS(
    SELECT departmentId, MAX(salary) as max_salary FROM Employee
    GROUP BY departmentId
)

SELECT Department.name AS Department, Employee.name AS Employee, DepartmentHighest.max_salary AS Salary 
FROM DepartmentHighest
JOIN Department ON DepartmentHighest.departmentId = Department.id
JOIN Employee ON DepartmentHighest.max_salary = Employee.salary
    AND Employee.departmentId = DepartmentHighest.departmentId