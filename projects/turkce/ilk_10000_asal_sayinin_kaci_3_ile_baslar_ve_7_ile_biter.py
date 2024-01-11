prime_liste=[2]
asal_sayi_sayaci=0
sayi=3
while asal_sayi_sayaci<10000:
    prime=True
    for i in range(2,sayi):
        if sayi%i==0:
            sayi+=1
            prime=False
            break
    if prime == True:
        prime_liste.append(sayi)
        asal_sayi_sayaci+=1
        sayi+=1
aranan_sayi=0
for sayii in prime_liste:
    if str(sayii).startswith("3") and str(sayii).endswith("7"):
        aranan_sayi+=1
print(aranan_sayi)




        

        
         
        



