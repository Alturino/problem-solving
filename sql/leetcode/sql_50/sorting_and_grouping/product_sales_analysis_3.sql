SELECT
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM sales AS s
WHERE
    (s.product_id, s.year) IN (SELECT
        s.product_id,
        min(year)
    FROM sales GROUP BY product_id)
