number = int(input("Enter a number: "))
str_number = str(number)
total = 0
for digit in str_number:
    total += int(digit)
print(total)
