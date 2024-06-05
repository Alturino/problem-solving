with id_and_count as (
    select
        employee_id,
        count(department_id) as count
    from employee group by employee_id
)

select
    e.employee_id,
    e.department_id
from employee as e
inner join id_and_count as ic
    on
        e.employee_id = ic.employee_id
        and (ic.count = 1 or e.primary_flag = 'Y');
