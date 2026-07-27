-- Write your PostgreSQL query statement below
WITH RateCount AS (
    SELECT user_id, COUNT(*) as rating_count FROM MovieRating
    GROUP BY user_id
),
GreatestRater AS(
    SELECT name FROM Users
    JOIN RateCount ON Users.user_id = RateCount.user_id
    WHERE RateCount.rating_count = (SELECT MAX(rating_count) FROM RateCount)
),
MovieAvgRating AS (
    SELECT movie_id, AVG(rating) as rating_avg FROM MovieRating
    WHERE created_at >= TO_DATE('01/02/2020', 'DD/MM/YYYY')
        AND created_at < TO_DATE('01/03/2020', 'DD/MM/YYYY')
    GROUP BY movie_id
),
HighestRating AS (
    SELECT title FROM Movies
    JOIN MovieAvgRating ON Movies.movie_id = MovieAvgRating.movie_id
    WHERE MovieAvgRating.rating_avg = (SELECT MAX(MovieAvgRating.rating_avg) FROM MovieAvgRating)
)

(SELECT name as results FROM GreatestRater
ORDER BY name ASC
LIMIT 1)
UNION ALL
(SELECT title as results FROM HighestRating
ORDER BY title ASC
LIMIT 1)