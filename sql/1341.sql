with GROUPEDVOTES as (
    select
        USER_ID,
        count(*) as CTS
    from MOVIERATING
    group by USER_ID
),

FSTRESULT as (
    select R.NAME as RESULTS
    from GROUPEDVOTES L
    left join USERS R on L.USER_ID = R.USER_ID
    order by L.CTS desc, R.NAME asc
    limit 1
),

RATEDMOVIES as (
    select
        L.TITLE,
        avg(R.RATING) as AVG_RATING
    from MOVIES L
    left join MOVIERATING R on L.MOVIE_ID = R.MOVIE_ID
    where
        R.CREATED_AT >= '2020-02-01'
        and R.CREATED_AT < '2020-03-01'
    group by L.TITLE
),

SCNDRESULT as (
    select TITLE as RESULTS
    from RATEDMOVIES
    order by AVG_RATING desc, TITLE asc
    limit 1
)

(select * from FSTRESULT)
union all
(select * from SCNDRESULT)
