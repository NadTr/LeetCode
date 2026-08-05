-- Write your PostgreSQL query statement below
WITH UserReactions AS (SELECT user_id, count(*) as cnt FROM reactions
    GROUP BY user_id),
ReactionsType AS (SELECT user_id, reaction, count(*) as cnt FROM reactions
    GROUP BY user_id, reaction)

SELECT UserReactions.user_id,
    ReactionsType.reaction as dominant_reaction, 
    ROUND(ReactionsType.cnt::numeric/ UserReactions.cnt, 2) as reaction_ratio
FROM UserReactions
JOIN ReactionsType ON UserReactions.user_id = ReactionsType.user_id
WHERE UserReactions.cnt >= 5
AND ReactionsType.cnt::numeric/ UserReactions.cnt >= 0.6
ORDER BY reaction_ratio desc, UserReactions.user_id asc
