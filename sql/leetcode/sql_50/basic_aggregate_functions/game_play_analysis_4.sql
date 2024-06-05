SELECT
    round(
        count(DISTINCT player_id)::numeric
        / (SELECT count(DISTINCT player_id) FROM activity)::numeric,
        2
    ) AS fraction
FROM activity
WHERE (player_id, (event_date - INTERVAL '1 day')) IN (
    SELECT
        player_id,
        min(event_date) AS first_login
    FROM activity
    GROUP BY player_id
);
