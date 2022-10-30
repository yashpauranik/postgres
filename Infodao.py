import psycopg2

def insert(infoObj):
    try:
        #establishing the connection
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO info_tbl(first_name, last_name,email,is_email_verified,mobile) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (infoObj[0], infoObj[1], infoObj[2] , infoObj[3] , infoObj[4])
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into info_tbl table")
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into info_tbl table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    return True
