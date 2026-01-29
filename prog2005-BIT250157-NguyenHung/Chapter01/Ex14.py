import math

try:
    number = float(input("Enter a number: "))
    if number < 0:
        print("Error: Negative number")
    else:
        print(math.sqrt(number))
except ValueError:
    print("Invalid input")