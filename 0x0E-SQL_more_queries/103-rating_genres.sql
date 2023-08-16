-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT name, SUM(tv_sr.rate) AS rating
FROM tv_genres AS tv_g
INNER JOIN tv_show_genres AS tv_sg
	ON tv_g.id = tv_sg.genre_id
INNER JOIN tv_show_ratings AS tv_sr
	ON tv_sg.show_id = tv_sr.show_id
GROUP BY name
ORDER BY rating DESC;
