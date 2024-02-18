-- Using JOIN
SELECT
    r.contest_id,
    round(
        (
            (count(r.user_id) * 100)::numeric
            / (SELECT count(user_id) FROM users)::numeric
        )::numeric,
        2
    ) AS percentage
FROM register AS r
INNER JOIN users AS u ON r.user_id = u.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;

-- -- Without JOIN
-- SELECT
--     r.contest_id,
--     round(
--         (
--             (count(r.user_id) * 100)::numeric
--             / (SELECT count(user_id) FROM users)::numeric
--         )::numeric,
--         2
--     ) AS percentage
-- FROM register AS r
-- GROUP BY r.contest_id
-- ORDER BY percentage DESC, r.contest_id ASC;
