-- Lists all shows contained in 'hbtn_0d_tvshows' that have at least one genre
-- Results must be sorted in ascending order by
--      'tv_shows.title' and
--      'tv_show_genres.genre_id'
-- The database name will be passed as an argument of the 'mysql' command
SELECT title, genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id ASC;
