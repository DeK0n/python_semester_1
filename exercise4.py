# 1 Numbers divided by 3

number = 1
while number <= 1000:
    modulo = number % 3
    if modulo == 0:
        print(str(number))
    number = number+1

# 2 Converter
inches_input = float(input("Enter length in inches: "))
while inches_input >=0:
    centimetres = inches_input * 2.54
    print(f"This lenght in cm is: {centimetres:.2f}")
    inches_input = float(input("Enter length in inches: "))

# 3 Sorting numbers

input_number = float(input("Enter 1st number: "))
smallest_number = input_number
largest_number = input_number
while input_number !="":
    if input_number <=smallest_number:
        smallest_number = input_number
    if input_number >=largest_number:
        largest_number = input_number
    input_number = input("Enter next number or leave empty string to finish: ")
    if input_number == "":
        break
    input_number = float(input_number)
print(f"The smallest number is: {smallest_number: 0.10f} and the largest number is: {largest_number: 0.10f}")

# 4 Guessing game

import random
random_integer = random.randint(1,10)
player_integer = int(input("Guess generated integer from 1 to 10: "))
while player_integer != random_integer:
    if player_integer < random_integer:
        print("Too low, try again")
    if player_integer > random_integer:
        print("Too high, try again")
    player_integer = int(input("Guess generated integer from 1 to 10: "))
print("Correct")

# 5 Username and passwrod checking

un = "python"
pw = "rules"
tries = 0
input_username = ""
input_password = ""
while not(input_username == un and input_password == pw):
    tries = tries+1
    input_username = input("Enter user name: ")
    input_password = input("Enter password: ")
    if tries ==5:
        print("Acsess denied")
        break
    elif input_username == un and input_password == pw:
        print("Welcome")
    else:
        print("Try again")

# 6 Pi
import math
import random
from turtle import position
operation_num = 0
n = 0
N = int(input("Enter number of points to generate: "))
while operation_num != N:
    operation_num = operation_num+1
    point_x = random.uniform(-1, 1)
    point_y = random.uniform(-1, 1)
    position = point_x*point_x+point_y*point_y
    if position < 1:
        n=n+1
pi = 4*n/N
print(pi)
