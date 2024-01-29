#iki sayili hesap makinesi 
a=int(input("ilk sayiyi giriniz:"))
b=int(input("siradaki sayiyi giriniz:"))

while True:
    islem=int(input("Hangi islemi yapmak istersiniz?\n \
    Eger toplama ise 1,\n \
    eger cikarma ise 2,\n \
    carpma ise 3,\n \
    bolme ise 4 girin! "))
    if islem == 1:
        print("Sonuc:",a+b)
        break
    elif islem == 2:
        print("Sonuc:",(a-b))
        break
    elif islem == 3:
        print("Sonuc:",a*b)
        break
    elif islem == 4:
        print("Sonuc:", a/b)
        break
    else:
        print("Tekrar deneyin")
         
    
