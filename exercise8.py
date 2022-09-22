#1
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town)
# from the airport database used on this course.

print("Input ICAO code to get iformation: ")

import mysql.connector

def getInfoByIcao(icao):
    sql = "SELECT name from airport where ident ='" + icao + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result) 
    return

# use your user and password, host can be localhost or 127.0.0.0
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='12332167',
         autocommit=True
         )

icao = input("Enter ICAO: ")
getInfoByIcao(icao)

#2
# Write a program that asks the user to enter the area code (for example FI)
#  and prints out the airports located in that country ordered by airport type. 
#  For example, Finland has 65 small airports, 15 helicopter airports and so on.

print("Input Area code to get iformation: ")

import mysql.connector

def getInfoById(id):
    sql = "SELECT type, name from airport where iso_country ='" + id + "' order by type desc"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result) 
    return

# use your user and password, host can be localhost or 127.0.0.0
connection = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='12332167',
         autocommit=True
         )

id = input("Enter ID: ")
getInfoById(id)

#3
# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. 
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.