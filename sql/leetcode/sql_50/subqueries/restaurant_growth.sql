with last_6_days as (
    select distinct visited_on from customer order by visited_on asc offset 6
)

select
    l.visited_on,
    sum(c.amount) as amount,
    round(sum(amount) / 7., 2) as average_amount
from last_6_days as l
inner join
    customer as c
    on c.visited_on between l.visited_on - 6 and l.visited_on
group by l.visited_on;
