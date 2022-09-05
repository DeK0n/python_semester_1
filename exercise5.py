# 1
# Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the
# the sum of the numbers. Use a for loop.

# import random
# dice_list = []
# dice_sum = 0
# rolls_total = int(input("How many times you want to throw dice?: "))
# rolls = 0
# while rolls != rolls_total:
#     rolls = rolls+1
#     dice_list.append(int(random.randint(1, 6)))
# for x in dice_list:
#     dice_sum = dice_sum+x
# print("The sum of all throws is: " + str(dice_sum) +" ("+ str(dice_list)+")")


# 2
# Write a program that asks the user to enter numbers until they input an empty string to quit. At the end,
#  the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order
#  of sorted list items by using the sort method with the reverse=True argument.

input_list = []
print("Input more than 5 numbers to get them sorted. Input empty string to quit.")
number_input = input("Input first number: ")
while number_input != "":
    input_list.append(number_input)
    number_input = input("Input next number or press Enter to quit: ")
input_list.sort(reverse=True)
print("Five greates numbers in descending order are: ")
for s in input_list[0:5]:
    print(s)

# 3
# Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are
#  number that are only divisible by one or the number itself.

# For example, number 13 is a prime number as can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.

# 4
# Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names)
#  and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city
#  per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate
#  through the list.
