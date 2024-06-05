SELECT
    p.product_id,
    coalesce(
        round(sum(p.price * u.units) / sum(units)::numeric, 2), 0
    ) AS average_price
FROM prices AS p
LEFT JOIN
    unitssold AS u
    ON
        p.product_id = u.product_id
        AND u.purchase_date BETWEEN p.start_date AND end_date
GROUP BY p.product_id
