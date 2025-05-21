-- Retrieve all playlists by a specific user
SELECT title FROM Playlist WHERE user_id = 1;

-- Retrieve all songs by a specific artist
SELECT * FROM Song WHERE artist = 'Burna Boy';

-- Retrieve all songs in a specific playlist
SELECT S.title, S.artist
FROM Song S
JOIN PlaylistSong PS ON S.song_id = PS.song_id
WHERE PS.playlist_id = 1;

-- Count total playlists per user
SELECT user_id, COUNT(*) AS total_playlists
FROM Playlist
GROUP BY user_id;

-- Search for songs by album
SELECT * FROM Song WHERE album = '1989';
