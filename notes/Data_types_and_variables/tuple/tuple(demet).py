tuple_1 = (3, 4.5, (6, 8.0), 'fkhf', "hello word")
print(tuple_1[0:3])  # Prints the elements from index 0 to index 2 (inclusive)
print(len(tuple_1))  # Prints the number of elements in tuple_1
for i in tuple_1:
    print(i)  # Prints each element of tuple_1

# Unlike lists, tuples cannot be modified after creation
# tuple_1[4] = 'hello' => This will result in an error

# The main difference between tuples and lists is that tuples are immutable
liste = [2, 'sfjfjf', 'ksjk']
liste[2] = 'fdfdfd'  # Lists can be modified
print(liste)  # Prints the modified list

