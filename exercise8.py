# 1
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town)
# from the airport database used on this course.

from geopy import distance
from unittest import result
import mysql.connector
print("Input ICAO code to get iformation: ")


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
    port=3306,
    database='flight_game',
    user='root',
    password='12332167',
    autocommit=True
)

icao = input("Enter ICAO: ")
getInfoByIcao(icao)

# 2
# Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.

print("Input Area code to get iformation: ")


def getInfoById(id):
    sql = "SELECT type, name from airport where iso_country ='" + \
        id + "' order by type desc"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return


# use your user and password, host can be localhost or 127.0.0.0
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='12332167',
    autocommit=True
)

id = input("Enter ID: ")
getInfoById(id)

# 3
# Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.  Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.

# version 3.2
print("Input ICAO codes of two airports to get iformation: ")
# use your user and password, host can be localhost or 127.0.0.0
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='12332167',
    autocommit=True
)


def getInfoBy(icao):
    sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# Version 3.0


icao = input("Enter 1st ICAO: ")
a = getInfoBy(icao)[0]
icao = input("Enter 2nd ICAO: ")
b = getInfoBy(icao)[0]
print(a, b)
print(f"The distance between is {distance.distance(a, b).km:.2f} km")

# def getInfoBy(icao1,icao2):
#     sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao1 + "'"
#     # print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result1 = cursor.fetchall()
#     print(result1)
#     sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao2 + "'"
#     # print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result2 = cursor.fetchall()
#     print(result2)
#     from geopy import distance
#     print(f"The distance between is {distance.distance(result1, result2).km:.2f} km")
#     return

# icao1 = input("Enter 1st ICAO: ")
# icao2 = input("Enter 2nd ICAO: ")
# getInfoBy(icao1,icao2)

# version 3.1
# def getInfoBy(icao):
#     sql = "SELECT latitude_deg, longitude_deg from airport where ident ='" + icao + "'"
#     # print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     return result

# icao = input("Enter 1st ICAO: ")
# for a in getInfoBy(icao):
#     a = a
# icao = input("Enter 2nd ICAO: ")
# for b in getInfoBy(icao):
#     b = b
# # print(a, b)
# print(f"The distance between is {distance.distance(a, b).km:.2f} km")
