import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="qweAsd33!", port="5432"
)

try:
    cur = conn.cursor()
    update_choice = input("update by (1) phone number or (2) user name? ")

    if update_choice == '1':
        current_phone = input("enter current phone number: ")
        new_phone = input("enter new phone number: ")

        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE phone = %s",
            (new_phone, current_phone)
        )

    elif update_choice == '2':
        current_name = input("enter current name: ")
        new_name = input("enter new name: ")

        cur.execute(
            "UPDATE phonebook SET name = %s WHERE name = %s",
            (new_name, current_name)
        )


    conn.commit()

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
