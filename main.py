# Testing grounds
from geopy import distance
from unittest import result
import mysql.connector

def listEurope():
    sql = 'SELECT name from countries where continent = "EU"'

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
    user='',
    password='',
    autocommit=True
)

listEurope()