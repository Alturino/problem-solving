with highest_salary as (
    select max(salary) as salary from employee
)

select max(e.salary) as "SecondHighestSalary"
from employee as e
where e.salary < (select salary from highest_salary)
