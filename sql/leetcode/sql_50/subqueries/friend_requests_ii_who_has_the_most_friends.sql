with total_friends as (
    select * from requestaccepted
    union all
    select
        case when 1 = 1 then accepter_id end as requester_id,
        case when 1 = 1 then requester_id end as accepter_id,
        accept_date
    from requestaccepted
)

select
    requester_id as id,
    count(*) as num
from total_friends
group by requester_id
order by num desc
limit 1;

-- with friend_count as (
--     select requester_id as id
--     from requestaccepted
--     union all
--     select accepter_id as id
--     from requestaccepted
-- )
--
-- select
--     id,
--     count(id) as num
-- from friend_count group by id order by num desc limit 1;
