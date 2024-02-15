a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = (a + b)
e = (a - b)
f = (a * b)
g = (a / b)
option = int(input("1-add/n2-subtract/n3-multiply/n4-divide"))
if option == 1:
    print(a + b)
    option = int(input("1-add/n2-subtract/n3-multiply/n4-divide"))
    if option == 1:
        print(d + c)
    elif option == 2:
        print(d - c)
    elif option == 3:
        print(d * c)
    elif option == 4:
        print(d / c)
elif option == 2:
    print(a - b)
    option = int(input("1-add/n2-subtract/n3-multiply/n4-divide"))
    if option == 1:
        print(e + c)
    elif option == 2:
        print(e - c)
    elif option == 3:
        print(e * c)
    elif option == 4:
        print(e / c)
elif option == 3:
    print(a * b)
    option = int(input("1-add/n2-subtract/n3-multiply/n4-divide"))
    if option == 1:
        print(f + c)
    elif option == 2:
        print(f - c)
    elif option == 3:
        print(f * c)
    elif option == 4:
        print(f / c)
else:
    print(a / b)
    option = int(input("1-add/n2-subtract/n3-multiply/n4-divide"))
    if option == 1:
        print(g + c)
    elif option == 2:
        print(g - c)
    elif option == 3:
        print(g * c)
    elif option == 4:
        print(g / c)

