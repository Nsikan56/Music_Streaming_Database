import pymysql
import bcrypt
from datetime import datetime
import os

# Establish connection
connection = pymysql.connect(
    host='localhost',
    user='your_user',
    password='your_password',
    database='music_streaming',
    cursorclass=pymysql.cursors.DictCursor
)

def safe_execute(query, values=None):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
        connection.commit()
        print("Query executed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def insert_user(username, password, email):
    try:
        if not all(isinstance(param, str) for param in [username, password, email]):
            raise ValueError("Username, password, and email must be strings")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        query = """
        INSERT INTO User (name, email) 
        VALUES (%s, %s)
        """
        safe_execute(query, (username, email))
        print("(Password hashed but not stored in table — see schema setup for secure design.)")
    except Exception as e:
        print(f"User insertion failed: {e}")

def insert_playlist(user_id, title):
    try:
        if not isinstance(user_id, int) or not isinstance(title, str):
            raise ValueError("user_id must be int, title must be str")
        query = """
        INSERT INTO Playlist (user_id, title)
        VALUES (%s, %s)
        """
        safe_execute(query, (user_id, title))
    except Exception as e:
        print(f"Playlist insertion failed: {e}")

def insert_song(title, artist, album, duration):
    try:
        if not all(isinstance(param, str) for param in [title, artist, album]) or not isinstance(duration, int):
            raise ValueError("Invalid song data types")
        query = """
        INSERT INTO Song (title, artist, album, duration)
        VALUES (%s, %s, %s, %s)
        """
        safe_execute(query, (title, artist, album, duration))
    except Exception as e:
        print(f"Song insertion failed: {e}")

def insert_playlist_song(playlist_id, song_id):
    try:
        if not isinstance(playlist_id, int) or not isinstance(song_id, int):
            raise ValueError("IDs must be integers")
        query = """
        INSERT INTO PlaylistSong (playlist_id, song_id)
        VALUES (%s, %s)
        """
        safe_execute(query, (playlist_id, song_id))
    except Exception as e:
        print(f"PlaylistSong link failed: {e}")

def insert_profile_image(user_id, image_url):
    try:
        if not isinstance(user_id, int) or not isinstance(image_url, str):
            raise ValueError("Invalid profile image parameters")
        query = """
        INSERT INTO ProfileImage (user_id, image_url)
        VALUES (%s, %s)
        """
        safe_execute(query, (user_id, image_url))
    except Exception as e:
        print(f"Profile image insertion failed: {e}")

if __name__ == '__main__':
    insert_user("john_doe", "password123", "john@example.com")
    insert_playlist(1, "My Favorites")
    insert_song("Shake It Off", "Taylor Swift", "1989", 242)
    insert_playlist_song(1, 1)
    insert_profile_image(1, "/images/john_profile.jpg")

    connection.close()
