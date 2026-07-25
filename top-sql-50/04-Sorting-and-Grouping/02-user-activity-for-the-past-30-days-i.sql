-- Write your PostgreSQL query statement below
SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users FROM Activity
WHERE activity_date BETWEEN TO_DATE('2019-07-27', 'YYYY-MM-DD') - INTERVAL '29 day' AND TO_DATE('2019-07-27', 'YYYY-MM-DD')
GROUP BY day