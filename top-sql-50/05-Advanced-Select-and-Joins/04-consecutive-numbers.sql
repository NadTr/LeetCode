-- Write your PostgreSQL query statement below
SELECT DISTINCT Logs.num as ConsecutiveNums 
FROM Logs
Join Logs as LogsOne ON Logs.id = (LogsOne.id + 1)
Join Logs as LogsTwo ON Logs.id = (LogsTwo.id + 2)
WHERE Logs.num = LogsOne.num AND Logs.num =LogsTwo.num
