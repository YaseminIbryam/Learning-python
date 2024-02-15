import math

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Floor Division (//)
# Exponentiation (**) or raising to power
# Square root (math.sqrt)
# Absolute value (abs)

# Rounding (rounding to a specified number of digits after the decimal point)
print(round(4.6198, 2))

# Modulus (%) (gives the remainder after division)
print(8 % 3)  # 8 divided by 3 equals 6 with a remainder of 2

# Displaying a float with a certain number of decimal places
print(f"{5385:.2f}")  # Using f-string to display a float with 2 decimal places
print("{:.4f}".format(3.53875385))  # Using format() to display a float with 4 decimal places

# Padding a number with leading zeros
seconds = 8
print(f"{seconds:02d}")  # Ensures that the number has 2 digits, padding with leading zeros if necessary

# Trigonometric functions
angle_in_degrees = 45
angle_in_radians = math.radians(angle_in_degrees)
sin_result = math.sin(angle_in_radians)
cos_result = math.cos(angle_in_radians)
tan_result = math.tan(angle_in_radians)

# Logarithm (base 2)
num = 8
result_logarithm = math.log2(num)
print(f"Logarithm (base 2) of {num}: {result_logarithm}")

# Factorial
n = 5
print(math.factorial(n))  # Calculates the factorial of a number
