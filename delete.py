import psycopg2


def deleteData(info_tableid):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        sql_delete_query = """Delete from info_table where id = %s"""
        cursor.execute(sql_delete_query, (info_tableid,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

id2 = 2
deleteData(id2)

