-- Write your PostgreSQL query statement below
SELECT id
    , SUM(revenue) FILTER(WHERE month = 'Jan') as Jan_revenue
    , SUM(revenue) FILTER(WHERE month = 'Feb') as Feb_revenue
    , SUM(revenue) FILTER(WHERE month = 'Mar') as Mar_revenue
    , SUM(revenue) FILTER(WHERE month = 'Apr') as Apr_revenue
    , SUM(revenue) FILTER(WHERE month = 'May') as May_revenue
    , SUM(revenue) FILTER(WHERE month = 'Jun') as Jun_revenue
    , SUM(revenue) FILTER(WHERE month = 'Jul') as Jul_revenue
    , SUM(revenue) FILTER(WHERE month = 'Aug') as Aug_revenue
    , SUM(revenue) FILTER(WHERE month = 'Sep') as Sep_revenue
    , SUM(revenue) FILTER(WHERE month = 'Oct') as Oct_revenue
    , SUM(revenue) FILTER(WHERE month = 'Nov') as Nov_revenue
    , SUM(revenue) FILTER(WHERE month = 'Dec') as Dec_revenue
FROM Department
GROUP BY id