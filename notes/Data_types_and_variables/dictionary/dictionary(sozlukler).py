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
del person["id"]  # Deleting a key.
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

# Accessing a key not in the dictionary without getting an error.
print(person.get("id", "not found"))  # You can also access keys that are in the dictionary.
# If a non-existent key is accessed, the text after the comma is printed.

