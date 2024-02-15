text = "  My name is Yasemin Ibryam. I live in Krumovgrad.  "
result = text.upper()  # Makes all letters uppercase
print(result)
result1 = text.lower()  # Makes all letters lowercase
print(result1)
result2 = text.title()  # Makes the first letter of each word uppercase
print(result2)
result3 = text.capitalize()  # Makes the first letter uppercase
print(result3)
result4 = text.islower()  # Are all letters lowercase?
print(result4)  # No
result5 = text.isupper()  # Are all letters uppercase?
print(result5)  # No
result6 = text.strip()  # Removes leading and trailing whitespace
print(result6)
result7 = text.split()  # Splits the text into a list of words based on whitespace
print(result7)
result8 = text.split(".")  # Splits the text into a list based on "."
print(result8)
result9 = "_".join(text)  # Joins the characters with underscores
print(result9)
result0 = text.index("Yasemin")  # Finds the index of a word or letter
print(result0)
result_ = text.startswith(" ")  # Checks if the text starts with a space
print(result_)
result11 = text.endswith(" ")  # Checks if the text ends with a space
print(result11)
result12 = text.replace("name", "ismim")  # Replaces a word with another word
print(result12)
result13 = text.replace("ı", "i").replace("ş", "s")  # Replaces characters with other characters
print(result13)
