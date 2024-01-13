for i in range(6, 16, 3):
    print(i)

string = "elif"
for i in string:
    print(i)

liste = ["Elif", "Tahsin", "Ibryam"]
for i in liste:
    print(i)

print(*range(0, 10, 2))

liste = range(20)
for i in liste:
    if i % 3 != 0:
        continue
    print(i)

# for-else
# eger for dongusu dogru bir sekilde calisip kirilmaz ise (yani break calismaz ise) donguden sonra else'e girilir
for i in range(57):
    if i == 10:
        print("broken")
        break

else:
    print("success for cycle wihtout break")
