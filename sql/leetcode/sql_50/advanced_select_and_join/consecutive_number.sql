select distinct l.num as consecutivenums
from logs as l
inner join logs as l2 on l.id = l2.id + 1
inner join logs as l3 on l2.id = l3.id + 1
where l.num = l2.num and l2.num = l3.num;
