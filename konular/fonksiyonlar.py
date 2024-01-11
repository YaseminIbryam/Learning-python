#finksiyon baslangici
 #/  fonksiyon ismi
def bilgi_ver():#parametre parantezi
    print("Islem basarili.") #kod blogu

#cagirma
bilgi_ver()


def selamla(isim):
    print("Merhaba " + isim)
selamla("JK")


def topla(x,y):
    print(f"x + y = {x + y}")

topla(3,8)

def selamla(mesaj, isim = "Anonim"): #opsiyonel,varsayilan
    print(f"{mesaj} {isim}")
selamla("merhaba")

def topla(x,y):
    return(x+y) #deger geri dondurmesi, eger tekrar kullanmak istersek diye
#topla(5,6) bu sekilde calismayacaktir cunki fonksiyonda print ifadesini kullanmadik 
topla56=topla(5,6)#return kullandigimzda fonksiyonu bir degiskene atayabliriz
print(topla56)
#fonksiyonlarda bir degiskene esitlenebilir
fonk=topla
print(fonk(2,3)) #ayni isi gorurler
    