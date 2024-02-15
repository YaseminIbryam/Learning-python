name = "Yasemin"
surname = "Ibryam"
age = "16"

# Concatenating strings
print(name + surname)  # Concatenates 'Yasemin' and 'Ibryam' without any space

# Concatenating strings with additional text
text = "My name is " + name + " and my surname is " + surname + ". I am " + age + "years old."
print(text)  # Concatenates strings with additional text

# Using the format() method for string formatting
print("My name is {} {}".format(name, surname))  # Inserts values of 'name' and 'surname' into the placeholders
print("My name is {1} {0}".format(name, surname))  # Inserts values in the specified order into placeholders
print("My name is {n} {s}".format(n=name, s=surname))  # Inserts values using named placeholders
print("My name is {} {}. I am {} years old.".format(name, surname, age))  # Inserts multiple values into placeholders
print("My name is {0} {1}. I am {2} years old. {2}".format(name, surname, age))  # Repeats the third value

# Using format() to control the formatting of numbers
number = 5/3
print("the result it is {n:1.6}".format(n=number))  # Formats the number with 6 decimal places

# Using f-strings (formatted string literals) for string formatting (available in newer Python versions)
# print(f"My name is {name} {surname) and I am {age} years old.")  # Uncomment this line in newer Python versions
