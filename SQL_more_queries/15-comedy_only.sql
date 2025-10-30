-- Script: 15-comedy_only.sql
-- Purpose: List all TV shows in the database hbtn_0d_tvshows that belong to the Comedy genre
-- Requirements:
--   - Display only show titles
--   - Sort alphabetically by title
--   - Use only ONE SELECT statement
--   - tv_genres contains only one row where name = 'Comedy' (id may vary)

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
