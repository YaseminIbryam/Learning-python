#benim yaptgim
sayi1,sayi2,sayi3,sayi4,sayi5=int(input("sayi girin:")),\
int(input("sayi girin:")),\
int(input("sayi girin:")),\
int(input("sayi girin:")),\
int(input("sayi girin:"))
Liste=[sayi1,sayi2,sayi3,sayi4,sayi5]
Liste.sort()
print(f"{Liste[0]} en kucuk sayi ve {Liste[4]} en buyuk sayidir")

#aslinda
liste=[]
for i in range(5):
    sayi=(int(input("sayi giriniz:")))
    liste.append(sayi)
print(f"en buyuk sayi {max(liste)}")
print(f"en kucuk sayi {min(liste)}")


