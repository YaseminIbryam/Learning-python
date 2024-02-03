# filter()
def is_even(number):
    return number % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)


# map()
def square(number):
    return number ** 2


nums = [1, 2, 3, 4, 5, 6, 7, 8]
squared_nums = list(map(square, nums))
print(squared_nums)