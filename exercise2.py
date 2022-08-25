import math
import random

#1
name = input('Enter your name:')
print('\n Hello, ' + name +'!')

#2
circle_radius = float(input('\n Write radius of the circle:'))
print(f"Area is {math.pi*circle_radius**2:.1f}")

#3
side_a = float(input('\n Write length of the rectangle: '))
side_b = float(input('Write width of the rectangle: '))
print(f"Perimeter of the rectangle is {side_a*2 + side_b*2:.0f} units and Area is {side_a*side_b:.0f} squared units")

#4
number_a = int(input('\n Enter an integer number 1: '))
number_b = int(input('Enter an integer number 2: '))
number_c = int(input('Enter an integer number 3: '))
print(f"The summ of three numbers is {number_a+number_b+number_c:.0f} , and the product is {number_a*number_b*number_c:.0f} and the average of them is {number_a*number_b*number_c/3:.0f} ")

#5
print("\n Enter weight in medieval talents, pounds and lots")
weight_talents = float(input('Enter talents: '))
weight_pounds = float(input('Enter pounds: '))
weight_lots = float(input('Enter lots: '))
weight_total_in_gramms = weight_talents*20*32*13.3+weight_pounds*32*13.3+weight_lots*13.3
weight_kilos = weight_total_in_gramms//1000 # "//" is division for integer result
weight_gramms_left = weight_total_in_gramms - weight_kilos*1000
print("The weight in modern units is: ")
print(f"{weight_kilos:.0f} kg and {weight_gramms_left: .2f} g")

#6
print("\n Here are some random numbers: ")
print(f"{random.randint(0, 999):03d}")
print(str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))