
# Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
#  We can define each season to last three months, December being the first month of winter.

# seasons = ("December","January","February","March","April","May","June","July","August","September","October","November")
# month = input("Write a month:")
# x = seasons.index(month)
# if 0<=x<=2:
#     print("Season is winter")
# if 3<=x<=5:
#     print("Season is spring")
# if 6<=x<=8:
#     print("Season is summer")
# if 9<=x<=11:
#     print("Season is autmn")

seasons = ("Winter","Spring","Summer","Autmn")
x=int(input("Type in month number:"))
if 0<=x<=2:
    print("Season is "+str(seasons[0]))
if 3<=x<=5:
    print("Season is "+str(seasons[1]))
if 6<=x<=8:
    print("Season is "+str(seasons[2]))
if 9<=x<=11:
    print("Season is "+str(seasons[3]))


# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending
# on whether the name was entered for the first time. Finally, the program lists out
# the input names one by one, one below another in any order. Use the set data structure to store the names.

names_list = set()
x = input("Enter name:")
while x != "":
    y = len(names_list)
    names_list.add(str(x))
    z = len(names_list)
    if z > y:
        print("New name")
    else:
        print("Existing name")
    x = input("Enter name:")
for q in names_list:
    print(q)

# 3
# Write a program for fetching and storing airport data. The program asks the user if
# they want to enter a new airport, fetch the information of an existing airport or quit.
#  If the user chooses to enter a new airport, the program asks the user to enter
#  the ICAO code and name of the airport. If the user chooses to fetch airport information instead,
#  the program asks for the ICAO code of the airport and prints out the corresponding name.
#  If the user chooses to quit, the program execution ends. The user can choose a new option as many times
#  they want until they choose to quit. (The ICAO code is an identifier that is unique to each airport.
#  For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes
#  of different airports online.)

dictionary ={}
print("Input 1 to enter new airport")
print("Input 2 to fetch information of existing airport")
print("Input 3 to exit")
command = int(input("Choose command:"))
while command !=3:
    if command == 1:
        print("input ICAO code and airport name")
        icao=input("ICAO: ")
        name=input("Name: ")
        dictionary[icao] = name
    elif command == 2:
        print("input ICAO to get name of the airport")
        icao=input("ICAO: ")
        print(dictionary[icao])
    else:
        print("Input error")
    command = int(input("Choose command:"))

    

