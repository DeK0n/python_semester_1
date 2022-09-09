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
    