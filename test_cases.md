# Test Cases – Music Streaming App

## ✅ Table Creation
- Tables created without syntax errors
- Primary keys and foreign key constraints enforced

## ✅ CRUD Operations
- Insert user with valid string parameters
- Insert song with valid string and numeric parameters
- Create playlist and link to user
- Associate song with playlist
- Insert profile image for user

## ✅ Query Testing
- Retrieve playlists by user ID
- Search for songs by artist and album
- Join query: fetch songs in playlist
- Count playlists per user

## ❌ Edge Cases
- Invalid input types (e.g., int for email)
- Duplicate keys (user_id, song_id) not allowed
- Deleting user: cascade delete on playlists
