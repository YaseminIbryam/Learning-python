import random

sayi=random.randint(1,100)
while True:
    tahmin=int(input("Tahmininizi yazin:"))
    if tahmin == sayi:
        print('Tebrikler, kazandiniz')
        break
    elif tahmin < sayi:
        print("Daha buyuk bir sayi giriniz")
    elif tahmin > sayi:
        print("Daha kucuk bir sayi giriniz")
    else: 
        print("Tekrar deneyin")