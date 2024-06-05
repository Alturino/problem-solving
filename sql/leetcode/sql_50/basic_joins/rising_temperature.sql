select distinct w2.id
from
    weather as w1,
    weather as w2
where
    w2.temperature > w1.temperature
    and w2.recorddate = w1.recorddate + 1;
