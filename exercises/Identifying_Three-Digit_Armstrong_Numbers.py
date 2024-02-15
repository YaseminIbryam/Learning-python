three_digit_numbers = []
for number in range(100, 1000):
    three_digit_numbers.append(number)
searched_numbers = []
for number in three_digit_numbers:
    str_number = str(number)
    digit1 = int(str_number[0]) ** 3
    digit2 = int(str_number[1]) ** 3
    digit3 = int(str_number[2]) ** 3
    if digit1 + digit2 + digit3 == number:
        searched_numbers.append(number)
print(searched_numbers)
print(len(searched_numbers))

