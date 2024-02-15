fibonacci_numbers = [1, 1]
index = 2
while len(str(fibonacci_numbers[-1])) <= 1000:
    fibonacci_numbers.append(fibonacci_numbers[index - 2] + fibonacci_numbers[index - 1])
    index += 1
    if len(str(fibonacci_numbers[-1])) == 1000:
        print(str(fibonacci_numbers[-1]))
        break
