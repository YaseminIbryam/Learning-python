# Numeric Types:

# int(integer) - Whole numbers: 1, -5, 100
int_number = 5
print(type(int_number))  # Prints: <class 'int'>

# float - Floating point numbers: 1.0, 9.6, -1.7
float_number = 35.7
print(type(float_number))  # Prints: <class 'float'>

# complex - Complex numbers: 5+8j
complex_number = complex(3, 7)
print(complex_number)  # Prints: (3+7j)
print(type(complex_number))  # Prints: <class 'complex'>

# decimal
# Example to avoid precision errors with floats:
a = 0.1
b = 0.2
c = 0.3
print(a + b + c)  # Prints: 0.6000000000000001
from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal('0.3')
print(a + b + c)  # Prints: 0.6
print(type(a))  # Prints: <class 'decimal.Decimal'>

# Text type: str(string)- "text", 'text'
string = "wow"
print(type(string))  # Prints: <class 'str'>

# List - Ordered and changeable collection: [123, 'abcd', 10.2, 'd']
list0 = [1, 3.4, "hello"]
print(type(list0))  # Prints: <class 'list'>

# Set - Unordered and unindexed collection
numbers = {1, 2, 3}

# Tuple - Ordered and unchangeable collection
tuple_example = ("how", 2, 1.0)
tuple_example2 = 5, 8, "hmm"
print(type(tuple_example))  # Prints: <class 'tuple'>
print(type(tuple_example2))  # Prints: <class 'tuple'>

# Dictionary(dict) - Ordered, changeable, and indexed collection
student_score = {'John': 85, 'Emily': 92, 'Sam': 78, 'Sarah': 90}
print(student_score['Sam'])  # Prints: 78

# bool(boolean)- True, False
boolean = True
print(type(boolean))  # Prints: <class 'bool'>

# bool() function
# Everything with a "value" is True
# Everything without a "value" is False
a = 5
print(bool(5))  # Prints: True
text = ""  # or text = None
print(bool(text))  # Prints: False
b = 0
print(bool(b))  # Prints: False
list1 = []

# isinstance() function checks if the specified object is of the specified type
print(isinstance('123', str))  # Prints: True
print(isinstance(123, str))  # Prints: False
print(isinstance(123 == 123, bool))  # Prints: True
