password = "abc1234567"
print(password[0])  # Prints the first character 'a'
print(password[-1])  # Prints the last character '7'
print(password[-2])  # Prints the second-to-last character '6'
print(password[0:5])  # Prints characters from index 0 to index 4 (exclusive), 'abc12'
print(password[3:8])  # Prints characters from index 3 to index 7 (exclusive), '12345'
print(password[:6])  # Prints characters from the beginning to index 5 (exclusive), 'abc123'
print(password[3:])  # Prints characters from index 3 to the end, '1234567'
print(password[-7:-2])  # Prints characters from index -7 to index -3 (exclusive), '23456'
print(password[0:7:2])  # Prints every second character from index 0 to index 6, 'ac246'
print(password[::2])  # Prints every second character from the beginning to the end, 'ac2467'
print(password[::-1])  # Reverses the string, '7654321cba'
print(len(password))  # Prints the length of the string, which is 10

# The len() function doesn't work with integers, it only works with strings, lists, tuples, etc.
# print(len(12))  # This will result in a TypeError.
