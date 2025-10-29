-- Script that lists all shows and their linked genre_id (if any)
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
-- Shows with no genre must still appear, with genre_id = NULL
-- Results sorted by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
