import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                        password="qweAsd33!", port="5432")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook(
    name VARCHAR(255), 
    phone VARCHAR(40) PRIMARY KEY
)
""")


conn.commit()

cur.close()
conn.close()