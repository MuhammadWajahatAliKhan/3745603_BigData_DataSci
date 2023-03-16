import psycopg2

conn = psycopg2.connect(database="youtube_database", user="postgres", password="postgres", host="localhost", port="5432")

cur = conn.cursor()


cur.execute("""
    SELECT title, view_count
    FROM videos
    ORDER BY view_count DESC
    LIMIT 10
""")
results = cur.fetchall()
print("Top 10 most viewed videos:")
for result in results:
    print(result)

cur.execute("""
    SELECT *
    FROM playlists
    WHERE published_at >= now() - interval '5 month'
""")
results = cur.fetchall()
print()
print("Playlists that were published in the last 5 months:")
for result in results:
    print(result)


cur.execute("""
    SELECT title, description
    FROM playlists
    WHERE published_at = (SELECT MAX(published_at) FROM playlists)
""")
result = cur.fetchone()
print()
print("title and description of the playlist with the most recent publication date:")
print("Latest Playlist: ", result[0], "-", result[1])


cur.execute("""
    SELECT title, NOW()::DATE - published_at::DATE as days_since_published
    FROM playlists
""")
results = cur.fetchall()
print()
print("playlists and the number of days since they were published:")
for result in results:
    print(result[0], " - Days Since Published: ", result[1])

cur.close()
conn.close()
