from typing import List, Any

liste = ["Python", 3, 9.0, "java", ("Hello", 30, "swo")]
# len fonksyonu (listenin kac elemandan olustugnu gosteriyor)
print(len(liste))

# listenin 1.elemaninin kac karakterden olustugnu gosteriyor
# print(len(liste[1]))  # int'te kullanilamaz

# accessing elements
print(liste[0])
print(liste[4])
print(liste[4][1])  # accessing elements in tuple in the list
print(liste[0:3])
print(liste[1::2])
print(liste[5:0:-2])

# searching for elements
just_list = [1, 2, 3, 4]
if 3 in just_list:
    print("Element 3 is in the list")

# METHODS

# append(listenin sonuna tek eleman eklememizi sagliyor)
liste.append("ok")
print(liste)

# insert(listenin istedigimiz indexine eleman eklememizi sagliyor)
liste.insert(2, "wow")  # listenin 2.nci indexine eleman eklemis olduk
print(liste)

# extend(listeyi baska bir liste ile ganisletmeye yariyor)
liste2 = ["lol", 29, 0]
liste.extend(liste2)  # liste2'yi liste'yin sonuna eklemis olduk
print(liste)

# remove(removes an element from list) note: if we have same element multiple times the method removes only one of them
liste.remove(9.0)
print(liste)

# pop(listedeki elemani indexi ile silmeye yariyor ve default olarak son elemani siliyor)
liste.pop(8)
print(liste)

# sort(elemanlarin alfabeye gore dizilmesine yariyor)
liste0 = ["hah", "ah", "mhm", "hmm"]
liste0.sort()  # liste0.sort(reverse=True) in this case it will reverse sorted elements
print(liste0)
# (sayilarda ise buyuklune gore)
liste1 = [3, 5, 7.5, 2]
liste1.sort()  # liste1.sort(reverse=True) in this case it will reverse sorted numbers
print(liste1)

# reverse(elemanlari tersine dizer)
liste0.reverse()
print(liste0)
liste1.reverse()
print(liste1)
# reversed (doesn't change the original version of the list, but you can use it as it is reversed)

# index(elemanlari aramamizi sagliyor)
print(liste.index(29))
# to not have value error when we search for element which is not in the list
try:
    print(just_list.index(3))
except ValueError:
    print("Element not found")

# count(listede o elemandan kac tane oldugunu bulmamiza yariyor)
sayi = [1, 4, 1, 6, 5, 2, 1, 3]
print(sayi.count(1))

# copy(bi listeden kopyalamaya yariyor)
harf = ["d", "g", "u", "w"]
harf1 = harf.copy()

print(harf1)

# clear(listeyi silmeye(bosaltmaya) yarar)
print(liste.clear())

# set() set is another data type (if are used the same values multiple times using this will remove the copies)
numbers = [1, 2, 3, 4, 2, 4, 5, 8, 3, 5, 6, ]
unique_numbers = list(set(numbers))
print(unique_numbers)

# *
digits = [4, 7, 2, 7, 6]
print(*digits)  # 4 7 2 7 6
print(*digits, sep='')  # 47276

# join - Concatenate any number of strings.
one_list = ['5', '9', '0']
one_string = '.'.join(one_list)
print(one_string)  # 5.9.0

# split
string = "wolf, sheep, sheep"
now_the_string_is_a_list = string.split(', ')  # split removes the (,) and ( ) from the sting in this case
print(now_the_string_is_a_list)  # ["wolf", "sheep", "sheep"]

some_text = "a b c d"
list_text = some_text.split(' ')
print(list_text)  # ['a', 'b', 'c', 'd']

# make list from input
nums = input().split(', ')
print(nums)  # prints nums as strings in list

# map
nums1 = list(map(int, input().split(', ')))
print(nums1)  # prints nums as integers in list

# something more
first, *second, third = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)  # 1
print(second)  # 2, 3, 4, 5, 6, 7, 8, 9
print(third)  # 10
