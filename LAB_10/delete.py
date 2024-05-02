import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="qweAsd33!",
    port="5432"
)

try:
    cur = conn.cursor()

    delete_choice = input("delete by (1) phone number or (2) user name? ")

    if delete_choice == '1':
        phone_to_delete = input("enter phone number to delete: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone_to_delete,))


    elif delete_choice == '2':
        name_to_delete = input("enter username to delete: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name_to_delete,))


    
    conn.commit()  

finally:
    if cur:
        cur.close()  # Close cursor
    if conn:
        conn.close()  # Close connection
