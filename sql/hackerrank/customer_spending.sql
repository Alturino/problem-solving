select
    c.customer_name,
    round(sum(i.total_price), 6) as amount
from customer as c
inner join invoice as i on c.id = i.customer_id
group by c.id, c.customer_name, i.total_price
having sum(i.total_price) < 0.25 * (select avg(total_price) from invoice)
order by round(sum(i.total_price), 6) desc;
