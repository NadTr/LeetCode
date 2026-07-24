SELECT Signups.user_id, 
    CASE 
        WHEN COUNT(TotalMessages.*) = 0 THEN 0 
        ELSE ROUND((COUNT(ConfirmedMessages.*)::NUMERIC)/COUNT(TotalMessages.*), 2) 
    END AS confirmation_rate

FROM Signups
LEFT JOIN Confirmations AS TotalMessages ON Signups.user_id = TotalMessages.user_id
LEFT JOIN Confirmations AS ConfirmedMessages 
    ON TotalMessages.user_id = ConfirmedMessages.user_id
    AND TotalMessages.time_stamp = ConfirmedMessages.time_stamp
    AND  ConfirmedMessages.action = 'confirmed' 

GROUP BY Signups.user_id
