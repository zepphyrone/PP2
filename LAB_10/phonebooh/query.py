import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="qweAsd33!",port="5432"
)

try:
    cur = conn.cursor()

    query_name = input("enter the name to query: ")


    cur.execute("SELECT * FROM phonebook WHERE name = %s", (query_name,))

    results = cur.fetchall()

    if results:
        for row in results:
            print("Name:", row[0], "Phone:", row[1])


finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
