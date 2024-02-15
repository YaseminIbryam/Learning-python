from typing import List, Any

# Creating a list with different data types.
my_list = ["Python", 3, 9.0, "Java", ("Hello", 30, "world")]

# len() function (shows the number of elements in the list).
print(len(my_list))

# Accessing elements.
print(my_list[0])  # Accessing the first element.
print(my_list[4])  # Accessing the fifth element.
print(my_list[4][1])  # Accessing elements in a tuple within the list.
print(my_list[0:3])  # Slicing the list.
print(my_list[1::2])  # Slicing the list with step 2.
print(my_list[5:0:-2])  # Slicing the list in reverse with step 2.

# Searching for elements.
just_list = [1, 2, 3, 4]
if 3 in just_list:
    print("Element 3 is in the list")

# METHODS

# append() (adds a single element to the end of the list).
my_list.append("ok")
print(my_list)

# insert() (inserts an element at the specified index).
my_list.insert(2, "wow")  # Inserting an element at index 2.
print(my_list)

# extend() (extends the list by appending elements from another list).
another_list = ["lol", 29, 0]
my_list.extend(another_list)  # Appending another_list to my_list.
print(my_list)

# remove() (removes an element from the list, only the first occurrence if there are duplicates).
my_list.remove(9.0)
print(my_list)

# pop() (removes the element at the specified index, or the last element by default).
my_list.pop(8)
print(my_list)

# sort() (sorts the elements alphabetically or numerically).
alpha_list = ["hah", "ah", "mhm", "hmm"]
alpha_list.sort()  # Sorting alphabetically.
print(alpha_list)
numeric_list = [3, 5, 7.5, 2]
numeric_list.sort()  # Sorting numerically.
print(numeric_list)

# reverse() (reverses the order of the elements).
alpha_list.reverse()
print(alpha_list)
numeric_list.reverse()
print(numeric_list)

# index() (returns the index of the specified element).
print(my_list.index(29))
try:
    print(just_list.index(3))
except ValueError:
    print("Element not found")

# count() (returns the number of occurrences of the specified element).
numbers = [1, 4, 1, 6, 5, 2, 1, 3]
print(numbers.count(1))

# copy() (returns a shallow copy of the list).
letters = ["d", "g", "u", "w"]
letters_copy = letters.copy()
print(letters_copy)

# clear() (removes all elements from the list).
print(my_list.clear())

# set() (returns a set, which is a collection with no duplicate elements).
numbers = [1, 2, 3, 4, 2, 4, 5, 8, 3, 5, 6]
unique_numbers = list(set(numbers))
print(unique_numbers)

# * (unpacking operator, used to unpack the elements of a list).
digits = [4, 7, 2, 7, 6]
print(*digits)  # Prints the elements separated by a space.
print(*digits, sep='')  # Prints the elements without any separation.

# join() (joins the elements of a list into a single string using a specified separator).
one_list = ['5', '9', '0']
one_string = '.'.join(one_list)
print(one_string)  # "5.9.0"

# split() (splits a string into a list).
string = "wolf, sheep, sheep"
now_the_string_is_a_list = string.split(', ')  # Splits the string at ', '
print(now_the_string_is_a_list)  # ["wolf", "sheep", "sheep"]

some_text = "a b c d"
list_text = some_text.split(' ')
print(list_text)  # ['a', 'b', 'c', 'd']

# make a list from input.
nums = input().split(', ')
print(nums)  # Prints input as strings in a list.

# map() (applies a function to all the items in an input list).
nums1 = list(map(int, input().split(', ')))
print(nums1)  # Prints input as integers in a list.

# Unpacking operator with more elements.
first, *second, third = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)  # 1
print(second)  # [2, 3, 4, 5, 6, 7, 8, 9]
print(third)  # 10
