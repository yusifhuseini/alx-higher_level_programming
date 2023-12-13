-- Lists all genres of the show 'Dexter'
-- Results must be sorted in ascending order by the genre name
-- The database name will be passed as an argument of the mysql command
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
    tv_shows.id = tv_show_genres.show_id
WHERE
    title = 'Dexter'
ORDER BY
    name ASC;
