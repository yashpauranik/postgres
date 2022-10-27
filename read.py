import psycopg2


def updateTable(nfo_tableid, mobilei):
	try:
		connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")


		cursor = connection.cursor()
		sql_update_query = """Update info_table set mobile = %s where id = %s"""
		cursor.execute(sql_update_query, (info_tableid,))
		connection.commit()
		count = cursor.rowcount
		print(count, "Record Updated successfully ")

	except (Exception, psycopg2.Error) as error:
		print("Error in update operation", error)

	finally:

		if connection:
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")


info_tableid = 1
mobile = 91
updateTable(info_tableid, mobile)
