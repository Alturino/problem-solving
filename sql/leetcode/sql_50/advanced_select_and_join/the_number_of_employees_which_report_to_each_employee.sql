select
    m.employee_id,
    m.name,
    count(m.employee_id) as reports_count,
    round(avg(e.age)::numeric) as average_age
from employees as m
inner join employees as e
    on m.employee_id = e.reports_to
group by m.employee_id, m.name
order by m.employee_id;
