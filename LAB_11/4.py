import psycopg2

def paginate_query(table_name, limit, offset):
    try:
        connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                                    password="a", port="5432"
        )

        cur = connection.cursor()

        query = f"SELECT * FROM {table_name} LIMIT %s OFFSET %s;"
        cur.execute(query, (limit, offset))
        
        rows = cur.fetchall()

        for row in rows:
            print(row)
            
    finally:
        if connection:
            cur.close()
            connection.close()

paginate_query('phone_book', limit=5, offset=0)