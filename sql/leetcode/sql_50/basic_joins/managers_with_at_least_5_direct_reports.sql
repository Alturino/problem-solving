select e1.name
from employee as e1
inner join employee as e2 on e1.id = e2.managerid
group by e1.name, e2.managerid
having count(e2.managerid) >= 5;
