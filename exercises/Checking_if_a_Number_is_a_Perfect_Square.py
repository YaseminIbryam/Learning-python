import math
number = int(input("Enter a number: "))
square_root = math.sqrt(number)
int_square_root = int(square_root)
if int_square_root == square_root:
    print("Perfect square")
else:
    print("Not a perfect square")



