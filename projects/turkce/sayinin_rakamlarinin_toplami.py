sayi=int(input("Sayi giriniz:"))
str_sayi=str(sayi)
toplam=0
for rakam in str_sayi:
    toplam+=int(rakam)
print(toplam)