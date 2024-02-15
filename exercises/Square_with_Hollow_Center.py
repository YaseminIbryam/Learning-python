size_of_square = int(input("Enter the size of the square:"))
for i in range(1, size_of_square + 1):
    if i == 1 or i == size_of_square:
        print(size_of_square * '*')
    else:
        print('*' + (size_of_square - 2) * ' ' + '*')
