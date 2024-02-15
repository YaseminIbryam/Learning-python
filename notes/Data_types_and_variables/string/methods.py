# String Methods:

# upper() - Converts all characters to uppercase
text = "hello world"
print(text.upper())  # Prints: HELLO WORLD

# lower() - Converts all characters to lowercase
text = "HELLO WORLD"
print(text.lower())  # Prints: hello world

# capitalize() - Converts the first character to uppercase, and the rest to lowercase
text = "hello world"
print(text.capitalize())  # Prints: Hello world

# title() - Converts the first character of each word to uppercase
text = "hello world"
print(text.title())  # Prints: Hello World

# swapcase() - Swaps the case of each character
text = "Hello World"
print(text.swapcase())  # Prints: hELLO wORLD

# strip() - Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
text = "  hello world  "
print(text.strip())  # Prints: hello world

# replace() - Replaces a specified value with another value in a string
text = "hello world"
print(text.replace("world", "Python"))  # Prints: hello Python

# split() - Splits the string into substrings if it finds instances of the separator
text = "hello world"
print(text.split())  # Prints: ['hello', 'world']

# join() - Joins the elements of an iterable to the end of the string
text = "-"
sequence = ("a", "b", "c")
print(text.join(sequence))  # Prints: a-b-c

# isalpha() - Returns True if all characters in the string are alphabetic
text = "hello"
print(text.isalpha())  # Prints: True

# isnumeric() - Returns True if all characters in the string are numeric
text = "12345"
print(text.isnumeric())  # Prints: True

# isalnum() - Returns True if all characters in the string are alphanumeric (either letters or numbers)
text = "hello123"
print(text.isalnum())  # Prints: True

# startswith() - Returns True if the string starts with the specified value
text = "hello world"
print(text.startswith("hello"))  # Prints: True

# endswith() - Returns True if the string ends with the specified value
text = "hello world"
print(text.endswith("world"))  # Prints: True
