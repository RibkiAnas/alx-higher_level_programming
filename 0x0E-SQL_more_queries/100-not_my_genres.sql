-- List all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT DISTINCT name
FROM tv_genres AS tv_g
INNER JOIN tv_show_genres AS tv_sg
	ON tv_g.id = tv_sg.genre_id
INNER JOIN tv_shows AS tv_s
	ON tv_s.id = tv_sg.show_id
WHERE tv_g.name NOT IN
	(SELECT name
		FROM tv_genres AS tv_g
		INNER JOIN tv_show_genres AS tv_sg
			ON tv_g.id = tv_sg.genre_id
		INNER JOIN tv_shows AS tv_s
			ON tv_s.id = tv_sg.show_id
		WHERE tv_s.title = 'Dexter')
ORDER BY name;
