import psycopg2

def search_records(pattern):
    try:
        connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                                    password="a", port="5432"
)

        cur = connection.cursor()

        query = "SELECT * FROM phone_book WHERE name LIKE %s OR phone_number LIKE %s"
        cur.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))

        records = cur.fetchall()

        return records

    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            cur.close()
            connection.close()

pattern = input()
matching_records = search_records(pattern)

for record in matching_records:
    print(record)