import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()
conn.autocommit = True
# cur.execute("DROP DATABASE youtube_database")
cur.execute("CREATE DATABASE youtube_database")
cur.execute("SELECT datname FROM pg_database")

conn.commit()

rows = cur.fetchall()
for row in rows:
    print(row[0])

cur.close()
conn.close()
