-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT title, SUM(tv_sr.rate) AS rating
FROM tv_shows AS tv_s
JOIN tv_show_ratings AS tv_sr
	ON tv_s.id = tv_sr.show_id
GROUP BY title
ORDER BY rating DESC
