select
    p.product_name,
    sum(o.unit) as unit
from products as p
inner join orders as o
    on p.product_id = o.product_id
where
    date_part('month', o.order_date) = '02'
    and date_part('year', o.order_date) = '2020'
group by p.product_id, p.product_name
having sum(o.unit) >= 100;
