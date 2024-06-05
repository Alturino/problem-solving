select
    s.machine_id,
    round(avg(e.timestamp - s.timestamp)::numeric, 3) as processing_time
from activity as s
inner join activity as e on s.machine_id = e.machine_id
where s.activity_type = 'start' and e.activity_type = 'end'
group by s.machine_id;
