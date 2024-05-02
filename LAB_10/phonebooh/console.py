import psycopg2


conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                        password="qweAsd33!", port="5432"
)

try:
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook(
            name VARCHAR(255), 
            phone VARCHAR(40) PRIMARY KEY
        )
    """)


    name = input("Enter your name: ")
    phone_number = input("Enter phone number: ")


    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone_number)
    )


    conn.commit()


finally:
    if cur:
        cur.close()
    if conn:
        conn.close()

