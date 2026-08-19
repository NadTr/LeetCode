-- Write your PostgreSQL query statement below
WITH session_datas AS(SELECT session_id,
        user_id, 
        (EXTRACT(EPOCH FROM (MAX(event_timestamp) - MIN(event_timestamp))) / 60) AS session_duration_minutes,
        COUNT(*) FILTER(WHERE event_type = 'scroll') as scroll_count,
        COUNT(*) FILTER(WHERE event_type = 'click')::numeric / COUNT(*) FILTER(WHERE event_type = 'scroll') as click_to_scroll_ration,
        COUNT(*) FILTER(WHERE event_type = 'purchase') as purchase
    FROM app_events
    GROUP BY session_id, user_id
    )
SELECT session_id, user_id, session_duration_minutes, scroll_count FROM session_datas
WHERE session_duration_minutes > 30
    AND scroll_count >= 5
    AND click_to_scroll_ration < 0.2
    AND purchase = 0
ORDER BY scroll_count DESC, session_id ASC