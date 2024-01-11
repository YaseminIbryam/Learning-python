sayi=int(input("sayi giriniz:"))
bolen=0
for i in range(1,sayi+1):
    if sayi%i == 0:
        bolen+=1
print(f"{sayi} sayisinin bolenleri {bolen}")
