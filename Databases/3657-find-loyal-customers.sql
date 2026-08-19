-- Write your PostgreSQL query statement below
SELECT customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING COUNT(transaction_id) >= 3
    AND MAX(transaction_date) - MIN(transaction_date) >= 30
    AND COUNT(transaction_id) FILTER(WHERE transaction_type = 'refund')::numeric / COUNT(transaction_id) < 0.2
ORDER BY customer_id ASC