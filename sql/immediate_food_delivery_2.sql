SELECT
    round(
        avg(
            CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END
        )::numeric * 100,
        2
    ) AS immediate_percentage
FROM delivery
WHERE (customer_id, order_date) IN (
    SELECT
        customer_id,
        min(order_date) AS min_order_date
    FROM delivery GROUP BY customer_id
);
