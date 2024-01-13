# int to float
result = float(16)
print(result)

# float to int
result = int(17.7)
print(result)

# bool to str
result = str(False)
print(result)
print(type(result))

# bool to int
result = int(False)
print(result)

# str to int
# harf içeren bir str int'e dönüşemez
a = "500"
# print(a+200) hata => a int olması gerek burda ise str
print(int(a) + 200)

print("400" * 4)  # => 4*400 işlemi i yapmaz sadece 400 4 kez yazar
print((int("400") * 4))  # =>
print(400 * 4)

# int to str
sayi = 20
sayi = str(sayi)
print(type(sayi))

# int to bool
# sayilarin hepsi bool'a donustutulunce True verir; 0 disinda, o False verir
number = 0
print(bool(number))

# str to bool
# sadece bos bir string False geri donusu yapar
text = ""
# print(bool(text))