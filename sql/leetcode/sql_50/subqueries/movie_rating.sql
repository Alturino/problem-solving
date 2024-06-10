with movierating_in_february_2020 as (
    select *
    from movierating
    where to_char(created_at, 'yyyy-mm') = '2020-02'
),

movie_title_with_highest_average_rating_in_february_2020 as (
    select movies.title
    from movierating_in_february_2020
    inner join movies
        on movierating_in_february_2020.movie_id = movies.movie_id
    group by movies.movie_id, movies.title
    order by
        avg(movierating_in_february_2020.rating) desc,
        movies.title asc
    limit 1
),

user_name_who_has_rated_the_greatest_number_of_movies as (
    select users.name
    from movierating
    inner join users
        on movierating.user_id = users.user_id
    group by users.user_id, users.name
    order by
        count(movierating.movie_id) desc,
        users.name asc
    limit 1
)

select name as results
from user_name_who_has_rated_the_greatest_number_of_movies
union all
select title
from movie_title_with_highest_average_rating_in_february_2020;
