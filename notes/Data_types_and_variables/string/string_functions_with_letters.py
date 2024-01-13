yazi = "  Benim adım Yasemin Ibryam. Koşukavak'da yasiyorum.  "
sonuc = yazi.upper()  # butun harfleri büyük yapiyor
print(sonuc)
sonuc1 = yazi.lower()  # butun harfleri küçük yapiyor
print(sonuc1)
sonuc2 = yazi.title()  # kelimelerin baş harflerini büyük yapiyor
print(sonuc2)
sonuc3 = yazi.capitalize()  # en baştaki harfi büyük yapiyor
print(sonuc3)
sonuc4 = yazi.islower()  # hepsi kuçük mü
print(sonuc4)  # hayır
sonuc5 = yazi.isupper()  # hepsi büyük mu
print(sonuc5)  # hayir
sonuc6 = yazi.strip()  # bastaki ve sondaki boşlukları yok ediyor
print(sonuc6)
sonuc7 = yazi.split()  # kelimeleri busluğa göre ayırıp dizi oluşturuyor
print(sonuc7)
sonuc8 = yazi.split(".")  # kelimeleri noktaya göre ayırıp dizi olusturuyor
print(sonuc8)
sonuc9 = "_".join(yazi)  # karkterlerin arasına sembol eklemek
print(sonuc9)
sonuc0 = yazi.index("Yasemin")  # kelime veya harf aratarak kaçını sirada olduğnu gosteriyor
print(sonuc0)
sonuc_ = yazi.startswith(" ")  # parantez içinde yazarak herhangi bir sembolle başlayıp baslamadiğini öğrenebiliriz
print(sonuc_)
sonuc11 = yazi.endswith(" ")  # parantez içinde yazarak herhangi bir sembolle bitip bitmediğini öğrenebiliriz
print(sonuc11)
sonuc12 = yazi.replace("adım", "ismim")  # bir kelimeyi veya harfi başka kelime veya harf ile değistirebiliyoruz
print(sonuc12)
sonuc13 = yazi.replace("ı", "i").replace("ş", "s")
print(sonuc13)
