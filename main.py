# shopping_list = ["apple", "celery", "spinach", "chicken"]
# print(shopping_list)
# shopping_list[3]="avocado"
# print(shopping_list)
# shopping_list.append("spinach")
# print(shopping_list)
# shopping_list.insert(0,"cabbage")
# print(shopping_list)
# shopping_list.pop(0)
# shopping_list.remove("spinach")
# print(shopping_list)

# name = []
# name = input("Enter your name:")
# index = 0
# while name != "" and index < len(name):
#     print(name[index])
#     index += 1

# name=input("Enter your name:")
# for character in name:
    # print(character)

# for number in range(1,10,2):
#     print(number)
# number=list(range(1,5))
# print(number)

# integer=int(input("Type in an integer:"))
# factorial=1
# while integer !=1:
#     factorial=factorial*integer
#     integer=integer-1
# if integer <=0:
#     break
# print(factorial)

integer=int(input("Type in integer:"))
factorial=1
if integer <=0:
    print("Your integer is <= 0, so bye bye!")
while integer>0:
    for x in range(1,(integer+1)):
      factorial=factorial*integer
      integer=integer-1
    print("The factorial of your integer is: " +str(factorial))
    factorial=1
    integer=int(input("Type in integer:"))
    