with quarters_volume as (
    select
        algorithm,
        sum(volume) as volume,
        quarter(dt) as quartal
    from coins as c
    inner join transactions as t on c.code = t.coin_code
    where year(dt) = 2020
    group by algorithm, volume, quarter(dt)
)

select
    qv1.algorithm,
    qv1.volume as q1,
    qv2.volume as q2,
    qv3.volume as q3,
    qv4.volume as q4
from quarters_volume as qv1
left join
    quarters_volume as qv2
    on qv1.algorithm = qv2.algorithm and qv2.quartal = 2
left join
    quarters_volume as qv3
    on qv1.algorithm = qv3.algorithm and qv3.quartal = 3
left join
    quarters_volume as qv4
    on qv1.algorithm = qv4.algorithm and qv4.quartal = 4
order by algorithm asc;
