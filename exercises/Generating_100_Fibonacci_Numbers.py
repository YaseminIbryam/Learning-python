fibonacci_numbers = []
while len(fibonacci_numbers) < 100:
    a = 1
    b = 1
    c = a + b
    fibonacci_numbers.append(a)
    fibonacci_numbers.append(b)
    fibonacci_numbers.append(c)
    while len(fibonacci_numbers) <= 100:
        a = b + c
        b = c + a
        c = a + b
        if len(fibonacci_numbers) < 100:
            fibonacci_numbers.append(a)
            if len(fibonacci_numbers) < 100:
                fibonacci_numbers.append(b)
                if len(fibonacci_numbers) < 100:
                    fibonacci_numbers.append(c)
        else:
            break
print(fibonacci_numbers)

