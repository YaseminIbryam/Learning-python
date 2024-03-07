person = {"name": "Ali", "age": 20, "gender": "m", "hobbies": ["cinema", "concert", "software"]}
# A dictionary consists of keys (first part) and values (second part).
# Values can contain any data type.
# Keys can only be of type string and integer.
print(person)
print(person["name"])  # Printing the value of the key "name" in the dictionary.
person["name"] = "Ahmet"  # Changing the value of the key.
print(person)
person.update({"age": 30, "name": "Mehmet"})  # Changing the values of several keys.
print(person)
person["id"] = 6878686  # Adding a new key and value.
print(person)

for key in person:
    print(key)  # Printing only the keys.

for key in person:
    print(person[key])  # Printing only the values.

print(person.keys())  # Printing the keys.
print(person.values())  # Printing the values.
print(person.items())  # Printing the keys and values together.

for key, value in person.items():  # Printing the keys and values together (with a for loop).
    print(key, value)


# Dictionary comprehensions
data = [("Peter", 22), ("Amy", 18), ("George", 35)]
dictionary = {key: value for key, value in data}
# {'Peter': 22, 'Amy': 18, 'George': 35}

# Methods
# copy - returns a copy of a dictionary
my_dict = {1: 'apple', 2: 'banana'}
copied_dict = my_dict.copy()
print(my_dict == copied_dict)  # True

# clear - removes all the elements from a dictionary
copied_dict.clear()
print(copied_dict)  # {}

# pop - removes and returns an item from a dictionary having the given key
my_dict = {"fruit": "apple", "vegetable": "cucumber"}
apple = my_dict.pop("fruit")  # 'apple'
print(my_dict)  # {'vegetable': 'cucumber'}

# popitem() - removes an item that was last inserted and returns it as a tuple - (key, value)
my_dict = {"fruit": "apple", "vegetable": "cucumber"}
print(my_dict.popitem())  # ("vegetable", "cucumber")
print(my_dict)  # {"fruit": "apple"}

# del keyword - removes an item with a specified key name
del person["id"]  # Deleting a key.
print(person)
# del keyword can also delete the dictionary completely (del dict)

# get; Accessing a value of key not in the dictionary without getting an error.
print(person.get("id", "not found"))  # You can also access keys that are in the dictionary.
# If a non-existent key is accessed, the data after the comma is returned.
# get can be used for adding not existing keys and extending them at the same time
netflix = {"series": ["Descendant of the sun", "Alice in Borderland"],
           "movies": ["Harry Potter", "The maze runner"]}
variable_we_are_searching_for = "series"
what_it_will_return_if_variable_is_missing = []
what_we_want_to_add_or_extend_with = "like extend for lists"
netflix[variable_we_are_searching_for] = netflix.get(variable_we_are_searching_for, what_we_want_to_add_or_extend_with) + [what_we_want_to_add_or_extend_with]
