-- Write your PostgreSQL query statement below
WITH FirstLogin AS(
    SELECT player_id, min(event_date) first_login
    FROM Activity
    GROUP BY player_id
)
SELECT ROUND( COUNT(Activity.player_id) FILTER(Where Activity.event_date  = FirstLogin.first_login + INTERVAL '1 day') *1.0 / (SELECT COUNT(*) FROM FirstLogin),2) as fraction
FROM Activity
LEFT JOIN FirstLogin ON Activity.player_id = FirstLogin.player_id
