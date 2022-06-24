import mysql.connector as sql
conn = sql.connect(
  host="localhost",
  user="root",
  password="2099"
)

if conn.is_connected():
    print("sucessfully connected")

conn.cursor().execute("CREATE DATABASE DVD5")
print("Database Successfully Created")
conn.cursor().execute("USE DVD5")
conn.cursor().execute('create table cd_details(year_of_release  int, type_of_movie  varchar(65) , movie_name varchar(65), language varchar(56))')
print("CD_table created")
conn.cursor().execute('create table dvd_detail(dvd_model varchar(65),dvd_name varchar(56),version int,range_of_amt int)')
print("DVD_table created")
conn.commit()


