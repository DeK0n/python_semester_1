#3
# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. 
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.

print("Input ICAO codes of two airports to get iformation: ")

from unittest import result
import mysql.connector

def getInfoBy(icao1,icao2):
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao1 + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result1 = cursor.fetchall()
    print(result1)
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao2 + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result2 = cursor.fetchall()
    print(result2)
    from geopy import distance
    print(f"The distance between is {distance.distance(result1, result2).km:.2f} km")
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

icao1 = input("Enter 1st ICAO: ")
icao2 = input("Enter 2nd ICAO: ")
getInfoBy(icao1,icao2)


