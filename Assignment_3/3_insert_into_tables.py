import psycopg2
import json

conn = psycopg2.connect(
    host="localhost",
    database="youtube_database",
    user="postgres",
    password="postgres",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE videos (
        id VARCHAR(255) PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        category_id VARCHAR(255),
        tags TEXT,
        published_at TIMESTAMP,
        view_count INT,
        like_count INT,
        comment_count INT
    )
""")

cursor.execute("""
    CREATE TABLE playlists (
        id VARCHAR(255) PRIMARY KEY,
        title VARCHAR(255),
        description TEXT,
        published_at TIMESTAMP
    )
""")

with open('vids.txt', 'r') as file:
    videos_response = json.loads(file.read())

with open('playlist.txt', 'r') as file:
    playlists_response = json.loads(file.read())

for video in videos_response['items']:
    video_id = video['id']
    title = video['snippet']['title']
    description = video['snippet']['description']
    category_id = video['snippet']['categoryId']
    tags = ",".join(video['snippet']['tags'])
    published_at = video['snippet']['publishedAt']
    view_count = video['statistics']['viewCount']
    like_count = video['statistics']['likeCount']
    comment_count = video['statistics']['commentCount']

    cursor.execute("""
        INSERT INTO videos (id, title, description, category_id, tags, published_at, view_count, like_count, comment_count)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (video_id, title, description, category_id, tags, published_at, view_count, like_count, comment_count))

for playlist in playlists_response['items']:
    playlist_id = playlist['id']
    title = playlist['snippet']['title']
    description = playlist['snippet']['description']
    published_at = playlist['snippet']['publishedAt']

    cursor.execute("""
        INSERT INTO playlists (id, title, description, published_at)
        VALUES (%s, %s, %s, %s)
    """, (playlist_id, title, description, published_at))

conn.commit()

conn.close()
