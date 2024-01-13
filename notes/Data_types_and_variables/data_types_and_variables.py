# Numeric Types:

# int(integer) - 1, -5, 100
int_number = 5
print(type(int_number))

# float - 1.0, 9.6, -1.7
float_number = 35.7
print(type(float_number))

# complex - 5+8j
complex_number = complex(3, 7)
print(complex_number)
print(type(complex_number))

# decimal
# if we want to do addition between float numbers there can be some mistakes

# example
a = 0.1
b = 0.2
c = 0.3
print(a + b + c)  # 0.6000000000000001, to make this doesn't happen we can use this:

from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal('0.3')
print(a + b + c)  # 0.6
print(type(a))

# Text type: str(string)- "yasi" , 'Yasi'
string = "wow"
print(type(string))

# List - [123, 'abcd', 10.2, 'd'] - can be change
list0 = [1, 3.4, "hello"]
print(type(list0))

# Set - unordered collection and unindexed
numbers = {1,  2, 3}

# Tuple - cannot be change
tuple_example = ("how", 2, 1.0)
tuple_example2 = 5, 8, "hmm"
print(type(tuple_example))
print(type(tuple_example2))


# Dictionary(dict) - ordered collection, changeable and indexed
student_score = {'John': 85, 'Emily': 92, 'Sam': 78, 'Sarah': 90}
print(student_score['Sam'])


# bool(boolean)-True, False
boolean = True
print(type(boolean))
# bool() function
# everything with a "value"is True
# everything without a "value"is False
a = 5
print(bool(5))  # True
text = ""  # or text = None
print(bool(text))  # False
b = 0
print(bool(b))  # False
list1 = []


# isinstance() function checks if the specified object is of the specified type
print(isinstance('123', str))  # True
print(isinstance(123, str))  # False
print(isinstance(123 == 123, bool))  # True