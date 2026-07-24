-- Write your PostgreSQL query statement below
SELECT Weather.id FROM Weather
Join Weather as YesterdayWeather on Weather.recordDate = YesterdayWeather.recordDate + INTERVAL '1 day'
WHERE Weather.temperature > YesterdayWeather.temperature
