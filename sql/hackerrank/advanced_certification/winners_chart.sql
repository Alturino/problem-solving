with ranked as (
    select
        event_id,
        participant_name,
        score,
        dense_rank() over (partition by event_id order by score desc) as ranking
    from (
        select
            event_id,
            participant_name,
            max(score) as score
        from scoretable
        group by event_id, participant_name
    ) as new_table
)

select
    event_id,
    group_concat(
        case when ranking = 1 then participant_name end
        order by participant_name
    ) as first,
    group_concat(
        case when ranking = 2 then participant_name end
        order by participant_name
    ) as second,
    group_concat(
        case when ranking = 3 then participant_name end
        order by participant_name
    ) as third
from
    ranked
group by event_id
order by event_id;
