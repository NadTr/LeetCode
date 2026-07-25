-- Write your PostgreSQL query statement below
SELECT to_char(trans_date, 'YYYY-MM') as month, country, 
    COUNT(*) as trans_count,
    COUNT(*) FILTER(WHERE state = 'approved') as approved_count, 
    SUM(amount) as trans_total_amount,
    COALESCE(SUM(amount) FILTER(WHERE state = 'approved') , 0) as approved_total_amount
FROM Transactions

GROUP BY month, country