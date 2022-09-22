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