# int to float
result = float(16)
print(result)  # Prints: 16.0

# float to int
result = int(17.7)
print(result)  # Prints: 17

# bool to str
result = str(False)
print(result)  # Prints: 'False'
print(type(result))  # Prints: <class 'str'>

# bool to int
result = int(False)
print(result)  # Prints: 0

# str to int
# A string containing letters cannot be converted to an integer
a = "500"
# print(a+200) # This will result in an error because 'a' needs to be an integer for addition
print(int(a) + 200)  # Prints: 700

print("400" * 4)  # This will concatenate '400' four times: '400400400400'
print((int("400") * 4))  # Converts '400' to an integer and multiplies it by 4: 1600
print(400 * 4)  # Multiplies 400 by 4: 1600

# int to str
number = 20
number = str(number)
print(type(number))  # Prints: <class 'str'>

# int to bool
# When converted to boolean, all numbers except 0 become True, while 0 becomes False
number = 0
print(bool(number))  # Prints: False

# str to bool
# Only an empty string evaluates to False
text = ""
# print(bool(text)) # This will print False because 'text' is an empty string
