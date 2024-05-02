import psycopg2 

def delete_data_by_pattern(pattern):
    try:
        connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", 
                                    password="a", port="5432"

        )
        
        cur = connection.cursor()

        query = """
            DELETE FROM phone_book 
            WHERE name = %s 
            OR surname = %s 
            OR phone_number = %s;
        """
        cur.execute(query, (pattern, pattern, pattern))
        
        deleted_rows = cur.rowcount
        print(f"Deleted {deleted_rows} rows.")

        connection.commit()

    finally:
        if connection:
            cur.close()
            connection.close()

pat = input('wo do you want to delete?')
delete_data_by_pattern(pat)