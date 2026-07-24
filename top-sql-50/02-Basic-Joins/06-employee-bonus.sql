-- Write your PostgreSQL query statement below
SELECT name, bonus FROM Employee
LEFT JOIN Bonus ON EMployee.empId = Bonus.empId
WHERE Bonus.bonus IS NULL 
    OR Bonus.bonus < 1000