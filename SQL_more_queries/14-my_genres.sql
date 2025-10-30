-- Script: 14-my_genres.sql
-- Purpose: List all genres of the show "Dexter" from the database hbtn_0d_tvshows
-- Requirements:
--   - Display only genre names
--   - Sort alphabetically
--   - Use a single SELECT statement
--   - tv_shows table contains only one row where title = 'Dexter'
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
