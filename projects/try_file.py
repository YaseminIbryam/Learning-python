def factorial(number):
    result = number
    for num in range(number - 1, 0, -1):
        result *= num
    return result


factorial(5)
