import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO info_table (id, first_name, last_name,email,is_email_verified,mobile) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (2, 'Yash','Pauranik' , 'yashpauranik@gmail.com', 'true' , 91)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into info_table table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into info_table table", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
