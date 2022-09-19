
#1
# Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.

import random
dice = 0
def dice_roll():
    random_dice = random.randint(1, 6)
    return random_dice
while dice != 6:
    dice=dice_roll()
    print(dice)
    
#2
# Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice. 
# The difference to the last exercise is that the dice rolling in the main program continues 
# until the program gets the maximum number on the dice, which is asked from the user at the beginning.

import random
dice = 0
def dice_roll(sides):
    random_dice = random.randint(1, sides)
    return random_dice
sides = int(input("Enter number of sides:"))
while dice != sides:
    dice=dice_roll(sides)
    print(dice)

#3
# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres. 
# Write a main program that asks for a volume in gallons from the user and converts the value to liters. 
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

def gasoline_convert(gallons):
    litres = gallons * 3.79
    return litres
gallons = float(input("Enter gallons:"))
while gallons >=0:
    x=gasoline_convert(gallons)
    print(str(x))
    gallons = float(input("Enter gallons:"))
    
#4
# Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. 
# For testing, write a main program where you create a list, call the function, and print out the value it returned.

def integer_list_sum(integer_list):
    sum=0
    for x in integer_list:
        sum=sum+x
    return sum

integer_list = [1,2,3,3,2,1]
print(str(integer_list_sum(integer_list)))

#5
# Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as 
# the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list,
#  call the function, and then print out both the original as well as the cut-down list.

def integer_list_changer(integer_list):
    new_list=[]
    for x in integer_list:
        if x%2 ==0:
            new_list.append(x)
    return new_list
integer_list=[1,2,3,4,5,6,7,8,9]
print(str(integer_list_changer(integer_list)))

#6
# Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros. 
# The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter 
# the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.

import math
def pizza_function(diameter,price):
    price_per_sqmeter=price/(math.pi*(diameter/200)**2)
    return price_per_sqmeter
print("Enter price(€) and diameters(cm) of two pizzas")
diameter = float(input("Enter diameter of the first pizza:"))
price = float(input("Enter price of the first pizza:"))
pizza_one = pizza_function(diameter,price)
diameter = float(input("Enter diameter of the second pizza:"))
price = float(input("Enter price of the second pizza:"))
pizza_two = pizza_function(diameter,price)
print(f"Price of the first pizza is {pizza_one:.2f} euros per square meter")
print(f"Price of the second pizza is {pizza_two:.2f} euros per square meter")
