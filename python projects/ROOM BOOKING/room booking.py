import mysql.connector
con =mysql.connector.connect(host ="localhost",user="root",passwd='2099',database='rms5')


c = con.cursor()

def checkin():
    d = input("Days:")
    g = input("Names :")
    a = input("Aadhar:")
    dt =input("Date :")
    b = input("Type :")
    data = (d,g,a,dt,b,data)
    V_sql_insert = "insert into checkin('"+d+"','"+g+"','"+a+"','"+dt+"','"+b+"')"
                    #c =con.cursor
    c.execute(V_sql_insert,data)
    con.commit()
    print("Data entered Succcessfully")


def checkout():
    b = input("Type & number :")
    tg = int(input("Guests :"))
    f = int(input("Fare :"))
    d = int(input("Days :"))
    bl = f*d*tg
    cod = input("Date:")
    data = (b,tg,f,d,bl,cod)
    V_sql_insert = "insert into checkin('"+b+"','"+tg+"','"+f+"','"+d+"','"+bl+"','"+cod+"')" 
    #c = con.cursor()
    c.execute(V_sql_insert,data)
    con.commit()
    print("Data Entered Successfully")

def rooms():
    print("Executive -5000/d/g")
    print(" ")
    print(""" Facilites provided --> wifi, TV,AC,Bathroom with all equipments,Breakfast,Lunch,Dinner""")
    print(" ")
    print("Deluxe - 2500/d/g")
    print(" ")
    print("""Facilites --> wifi, TV,AC,separate Bathroom, Breakfast, Lunch,Dinner""")
    print(" ")
    print("simple- 1000/d/g")
    print("""Facilites --> TV, AC, Separate Bathroom""")


def main():
    print("1. Check In")
    print("2. Check Out")
    print("3.Fare and Amenities")
    c = int(input("choice :"))
    if c == 1:
        checkin()
    elif c == 2:
        checkout()
    elif c == 3:
        rooms()
    else:
        print("Enter correct Choice")

main()
