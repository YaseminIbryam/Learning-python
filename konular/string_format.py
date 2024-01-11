name = "Yasemin"
surname = "Ibryam"
age = "16"

print(name + surname)

text = "Benim adım " + name + " ve soyadim " + surname + ". Yasim ise " + age + "."
print(text)


name = "Yasemin"
surname = "Ibryam"
age = "16"
print("My name is {} {}".format(name, surname))
print("My name is {1} {0}".format(name, surname))
print("My name is {n} {s}".format(n=name, s=surname))
print("My name is {} {}. I am {} years old.".format(name, surname, age))
print("My name is {0} {1}. I am {2} years old. {2}".format(name, surname, age))

number = 5/3
print("the result it is {n:1.6}" . format(n=number))
#print(f"My name is {name} {surname) and I am {age} years old.") YENİ GUNCELLEMEDE KULLANILIYOR
