import math
n = int(input("number?"))
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        print(f"dividable by {i}")
        break
else:
    print("prime")