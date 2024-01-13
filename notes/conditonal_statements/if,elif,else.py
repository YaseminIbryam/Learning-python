a = 5
b = 8
c = 10
if a > b or c > a:
    print("true")
elif a == b and b == c:
    print("yes")
else:
    print("false")

# only valid for if - else
first_number = 6
second_number = 10
result = "first number is greater" if first_number > second_number else "second number is greater or numbers are equal"
print(result)