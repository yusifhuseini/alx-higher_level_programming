-- List all genres not linked to the show Dexter
-- Results must be sorted in descending order by their rating
-- The database name will be passed as an argument of the mysql command
SELECT
    name
FROM
    tv_genres
WHERE
    name NOT IN
    (
        SELECT
            name
        FROM
            tv_genres
        LEFT JOIN
            tv_show_genres
        ON
            tv_genres.id = tv_show_genres.genre_id
        LEFT JOIN
            tv_shows
        ON
            tv_show_genres.show_id = tv_shows.id
        WHERE 
            tv_shows.title = 'Dexter'
    )
ORDER BY
    name ASC;
