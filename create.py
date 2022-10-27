import boto3
conn = psycopg2.connect(
   database="postgres", user='postgres', password='1234', host='127.0.0.1', port= '5432'
)

cursor = conn.cursor()

#
cursor.execute("DROP TABLE IF EXISTS info_table")


sql ='''CREATE TABLE info_table(
   id integer PRIMARY KEY NOT NULL,
   first_name varchar(15) NOT NULL,
   last_name varchar(20) NOT NULL,
   email varchar(25),   
   is_email_verified Boolean,
   mobile bigint
)'''
cursor.execute(sql)
conn.commit()
conn.close()