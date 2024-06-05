with default_price as (
    select
        product_id,
        change_date,
        nullif(new_price, 10) as price
    from products
    where (product_id, change_date) in (select
        product_id,
        max(change_date)
    from products where change_date::date <= '2019-08-16' group by product_id)
)

select distinct
    product_id,
    coalesce(p1.price, 10) as prices
from default_price as p1
right join products as p2 on p1.product_id = p2.product_id
order by p2.product_id;
