# basic calculator with two numbers
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

while True:
    operator = int(input("What do you want to do?\n \
    For addition enter 1,\n \
    For subtraction enter 2,\n \
    For multiplication enter 3,\n \
    For division enter 4!"))
    if operator == 1:
        print("Result:", a + b)
        break
    elif operator == 2:
        print("Result:", (a - b))
        break
    elif operator == 3:
        print("Result:", a * b)
        break
    elif operator == 4:
        print("Result:", a / b)
        break
    else:
        print("Try again")
