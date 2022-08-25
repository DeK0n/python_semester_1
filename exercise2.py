#1
# name = input('Enter your name:')
#print('Hello, ' + name +'!')

#2
# import math
#circle_radius = float(input('Write radius of the circle:'))
#print(f"Area is {math.pi*circle_radius**2:.1f}")

#3
#side_a = float(input('Write length of the rectangle: '))
#side_b = float(input('Write length of the rectangle: '))
#print(f"Perimeter of the rectangle is {side_a*2 + side_b*2:.0f} units and Area is {a*b:.0f} squared units")

#4
#number_a = int(input('Enter an integer number 1: '))
#number_b = int(input('Enter an integer number 2: '))
#number_c = int(input('Enter an integer number 3: '))
#print(f"The summ of three numbers is {number_a+number_b+number_c:.0f} , and the product is {number_a*number_b*number_c:.0f} and the average of them is {number_a*number_b*number_c/3:.0f} ")

#5
print("Enter weight in medieval talents, pounds and talents")
weight_talents = float(input('Enter talents: '))
weight_pounds = float(input('Enter pounds: '))
weight_lots = float(input('Enter lots: '))
print("The weights in modern units are: ")
weight_total_in_gramms = weight_talents*20*32*13.3+weight_pounds*32*13+weight_lots*13.3
weight_kilos = int(weight_total_in_gramms/1000)
print(weight_kilos)
weight_gramms_left = weight_total_in_gramms - weight_kilos*1000
print(f"The weight in modern units is:  {weight_kilos} kg and {weight_gramms_left: .2f} gramms")



#6
# import random
#print(f"{random.randint(0, 999):03d}")
#print(str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))



