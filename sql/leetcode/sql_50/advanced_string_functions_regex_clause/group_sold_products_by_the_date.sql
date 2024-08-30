select
    sell_date,
    count(distinct sell_date) as num_sold,
    string_agg(distinct product, ',' order by product asc) as products
from activities
group by sell_date
order by sell_date asc;
