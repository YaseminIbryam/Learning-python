text = input("Enter text: ")
for i in text:
    if i == "a":
        text = text.replace("a", "A")
    else:
        continue
print(text)

    