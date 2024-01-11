 #Sayi tahmin oyunu
print("Sayi tahmin oyunu oynmak istermisin")
print("Cevabiniz evet ise lutfen e yazin,cevabiniz hayir ise h yazin")
while True:
    cevabiniz=input("Cevabiniz:")
    if cevabiniz== "h":
        print("Peki,birdaki sefere")
        break
    elif cevabiniz=="e":
        while True:
            sayi=9631
            
            tahmininiz=int(input("tahmininizi yazin:"))
            if sayi>tahmininiz:
                print("lutfen daha buyuk bir sayi giriniz")
            elif sayi<tahmininiz:
                print("lutfen daha kucuk bir sayi giriniz")
            elif sayi==tahmininiz:
                print("tebrikler,kazandiniz:)")
                break
    else:
        print("anlamadim,lutfen tekrar deneyin")
        continue
    break