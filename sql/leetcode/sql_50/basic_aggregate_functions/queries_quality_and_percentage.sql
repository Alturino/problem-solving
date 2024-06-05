SELECT
    query_name,
    round(
        avg(rating::numeric / position::numeric),
        2
    ) AS quality,
    round(
        avg(CASE WHEN rating < 3 THEN 1 ELSE 0 END)::numeric * 100, 2
    ) AS poor_query_percentage
FROM queries
WHERE query_name IS NOT null
GROUP BY query_name;
