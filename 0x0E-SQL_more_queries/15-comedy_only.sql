-- Lists all Comedy shows in the database hbtn_0d_tvshows
-- Results must be sorted in ascending order by the show title
-- The database name will be passed as an argument of the mysql command
SELECT
    title
FROM
    tv_shows
INNER JOIN
    tv_show_genres
ON
    tv_shows.id = tv_show_genres.show_id
INNER JOIN
    tv_genres
ON
    tv_genres.id = tv_show_genres.genre_id
WHERE
    tv_genres.name = "Comedy"
ORDER BY
    title ASC;
