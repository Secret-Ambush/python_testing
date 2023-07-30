import psycopg2

conn = psycopg2.connect(database="TestDB",
                        host="localhost",
                        user="postgres",
                        password="a",
                        port="5432")

cursor = conn.cursor()
cursor.execute("SELECT * FROM testing")
print(cursor.fetchall())