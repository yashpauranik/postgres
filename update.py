import psycopg2

def updateTable(info_tableid, mobile):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        sql_select_query = """select * from info_table where id = %s"""
        cursor.execute(sql_select_query, (info_tableid,))
        record = cursor.fetchone()



        sql_update_query = """Update info_table set mobile = %s where id = %s"""
        cursor.execute(sql_update_query, (mobile, info_tableid))
        connection.commit()
        count = cursor.rowcount


        sql_select_query = """select * from info_table where id = %s"""
        cursor.execute(sql_select_query, (info_tableid,))
        record = cursor.fetchone()


    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:

        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

id = 2
mobile = 99
updateTable(id, mobile)
