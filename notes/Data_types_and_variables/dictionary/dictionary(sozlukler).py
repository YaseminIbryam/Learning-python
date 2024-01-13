kisi = {"isim": "ali", "yas": 20, "cinsiyet": "m", "hobiler": ["sinema", "konser", "yazilim"]}
# keys(ilk kisim) ve value(ikinci kisim) kisimlarindan olusur
# value butun veri turunu icerebilir
# keys kismi sadece string ve int tipinde olabilir
print(kisi)
print(kisi["isim"])  # sozlukteki isim(key)'in degerini(value) yazdiriyor
kisi["isim"] = "ahmet"  # keyin degerini degistiriyor
print(kisi)
kisi.update({"yas": 30, "isim": "mehmet"})  # birkac keyin degerini degistiriyor
print(kisi)
kisi["id"] = 6878686  # yeni key ve degerini eklemek
print(kisi)
del kisi["id"]  # bir keyi siliyor
print(kisi)

for i in kisi:
    print(i)  # sadece keyleri yazdiriyor

for i in kisi:
    print(kisi[i])  # sadece valueleri yazdiriyor

print(kisi.keys())  # keys yazdiriyor
print(kisi.values())  # values yazdiriyor
print(kisi.items())  # keys ve values eslestirip yazdiriyor

for i in kisi.items():  # keys ve values eslestirip yazdiriyor(for dongusu ile)
    print(i)

for i, k in kisi.items():  # keys ve values eslestirip yazdiriyor(for dongusu ile) daha iyi bir sekilde
    print(i, k)

for key, value in kisi.items():
    print(key, value)

# hata almadan sozlukte olmayan key cagirma
print(kisi.get("id", "yok"))  # sozlukte olan key de cagrilabilir
# eger olmayan key cagrildiysa virgul ile ayirdiktan sonra yazilan yazdirilir
