import psycopg2
import csv

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                        password="qweAsd33!", port="5432"
)

try:
    cur = conn.cursor()

    cur.execute("ALTER TABLE phonebook ALTER COLUMN phone TYPE VARCHAR(20);")

    csv_file_path = 'phonebook.csv'
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            name, phone = row
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (name, phone)
            )


    conn.commit()



finally:
    if cur:
        cur.close()
    if conn:
        conn.close()

