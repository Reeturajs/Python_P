import mysql.connector
con = mysql.connector.connect(host="localhost", user='root', passwd='2099')
c = con.cursor()
sql1 = "create database rms5"
c.execute(sql1)
sql2 = "use rms5"
c.execute(sql2)
sql3 = "create table checkin (days varchar(50),names varchar(20),aadhaar bigint,date int,type varchar(20) )"
c.execute(sql3)
sql4 = "create table checkout (type varchar(20),guests integer,fare integer,days integer,tbill integer,date int)"
c.execute(sql4)
con.commit()
