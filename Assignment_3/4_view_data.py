import psycopg2

conn = psycopg2.connect(database="youtube_database", user="postgres", password="postgres", host="localhost", port="5432")

cur = conn.cursor()

cur.execute("SELECT * FROM playlists")
rows = cur.fetchall()
print("playlists Table:")
for row in rows:
    print(row)

cur.execute("SELECT * FROM videos")
rows = cur.fetchall()
print("Videos Table:")
for row in rows:
    print(row)

cur.close()
conn.close()
