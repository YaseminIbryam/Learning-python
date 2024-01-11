faktoriyel=1
while True:
    sayi=int(input("pozitif bir sayi giriniz:"))
    if sayi <=0:
        continue
    else:
        for i in range(1,sayi+1):
            faktoriyel *= i #faktoriyel=i*faktoriyel
        print("faktoriyel",faktoriyel)
        break
    