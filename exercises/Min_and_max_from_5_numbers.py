# First version
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))
number4 = int(input("Enter a number: "))
number5 = int(input("Enter a number: "))
list_numbers = [number1, number2, number3, number4, number5]
list_numbers.sort()
print(f"The smallest number is {list_numbers[0]} and the largest number is {list_numbers[4]}")

# Better version
number_list = []
for i in range(5):
    number = int(input("Enter a number: "))
    number_list.append(number)
print(f"The largest number is {max(number_list)}")
print(f"The smallest number is {min(number_list)}")


