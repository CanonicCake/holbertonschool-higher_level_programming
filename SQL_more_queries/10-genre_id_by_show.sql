-- Lists all shows within hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genres_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show.id
WHERE tv_show_genres.genres_id IS NOT NULL
ORDER BY tv_shows.title, tv_show_genres.genres_id;