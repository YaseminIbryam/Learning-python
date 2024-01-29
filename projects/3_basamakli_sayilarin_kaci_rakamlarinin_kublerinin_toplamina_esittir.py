basamakli3=[]
for sayi in range(100,1000):
    basamakli3.append(sayi)
aranan_sayilar=[]
for sayi in basamakli3:
    strsayi=str(sayi)
    rakam1=int(strsayi[0])**3
    rakam2=int(strsayi[1])**3
    rakam3=int(strsayi[2])**3
    if rakam1+rakam2+rakam3==sayi:
        aranan_sayilar.append(sayi)
print(aranan_sayilar)
print(len(aranan_sayilar))