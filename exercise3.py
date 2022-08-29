#1 Fish length
fish_length = int(input("Enter your zander's length in centimeters:"))
limit = 42
length_missing = limit - fish_length
if fish_length < limit:
    print("Release the fish into the lake, it must be larger by " + str(length_missing)+" centimeters." )
else:
    print("The fish is over 42cm and fits limit.")

#2 Cabin class
cabin_class = input("Enter the cabin class(LUX, A, B or C): ")
class_lux = "LUX"
class_a = "A"
class_b = "B"
class_c = "C"
if cabin_class == class_lux:
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == class_a:
    print("A: above the car deck, equipped with a window.")
elif cabin_class == class_a:
    print("B: windowless cabin above the car deck.")
elif cabin_class == class_a:
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#3 Hemoglobin value
person_gender = input("Enter your biological gender (M or F):")
person_gv = int(input("Enter your hemoglobin value (g/l):"))
if person_gender == "M":
    if person_gv <= 167 and person_gv >= 134:
        print("Hemoglobin value is normal.")
    elif person_gv > 167:
        print("Hemoglobin value is high.")
    elif person_gv < 134:
        print("Hemoglobin value is low.")
elif person_gender == "F":
    if person_gv <= 155 and person_gv >= 117:
        print("Hemoglobin value is normal.")
    elif person_gv > 155:
        print("Hemoglobin value is high.")
    elif person_gv < 117:
        print("Hemoglobin value is low.")
else:
    print("Input error.")

#4 Leap year
year = int(input("Enter a year number to check if it is leap: "))
division_modulo_4 = year % 4
division_modulo_100 = year % 100
division_modulo_400 = year % 400
if division_modulo_4 == 0:
    if division_modulo_100 == 0 and division_modulo_400 != 0:
        print("The year is NOT leap")
    else:
        print("The year is LEAP")
else:
    print("The year is NOT leap.")





    