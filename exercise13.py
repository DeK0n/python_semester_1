from flask import Flask, request
import math
import json
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='12332167',
    autocommit=True
)
@app.route('/prime_check/<number>')
def prime_check(number):
    prime = False
    number = int(number)

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
            else:
                prime = True
    response = {"Number": number, "isPrime": prime}
    return response


# @app.route('/test/<test>')
# def test_check(test):
#     response = test
#     return response

@app.route('/airport/<icao>')
def airport_check(icao):
    sql = "SELECT name, municipality from airport where ident ='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    response1 = cursor.fetchall()
    for i in response1:
        name = i[0]
        location = i[1]
    response = '{"ICAO":"'+icao+'", "Name":"'+name+'", "Location":"'+location+'"}'
    return response 

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
