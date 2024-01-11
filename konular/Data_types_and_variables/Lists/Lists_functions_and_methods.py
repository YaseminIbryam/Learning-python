liste = ["Python", 3, 9.0, "java", ("Hello", 30, "swo")]
# len fonksyonu (listenin kac elemandan olustugnu gosteriyor)
print(len(liste))

# listenin 1.elemaninin kac karakterden olustugnu gosteriyor
# print(len(liste[1]))  # int'te kullanilamaz

# elemanlara ulasma
print(liste[0])
print(liste[4])
print(liste[4][1])  # listedeki tuple'in elemanina ulasma
print(liste[0:3])
print(liste[1::2])
print(liste[5:0:-2])


# METODLAR

# append(listenin sonuna tek eleman eklememizi sagliyor)
liste.append("ok")
print(liste)

# insert(listenin istedigimiz indexine eleman eklememizi sagliyor)
liste.insert(2, "wow")  # listenin 2.nci indexine eleman eklemis olduk
print(liste)

# extend(listeyi baska bir liste ile ganisletmeye yariyor)
liste2 = ["lol", 29, 0]
liste.extend(liste2)  # liste2'yi liste'yin sonuna eklemis olduk
print(liste)

# remove(listedeki elemani silmeye yariyor)
liste.remove(9.0)
print(liste)

# pop(listedeki elemani indexi ile silmeye yariyor ve default olarak son elemani siliyor)
liste.pop(8)
print(liste)

# sort(elemanlarin alfabeye gore dizilmesine yariyor)
liste0 = ["hah", "ah", "mhm", "hmm"]
liste0.sort()
print(liste0)
# (sayilarda ise buyuklune gore)
liste1 = [3, 5, 7.5, 2]
liste1.sort()
print(liste1)

# reverse(sort metodunun aksine elemanlari tersine dizer)
liste0.reverse()
print(liste0)
liste1.reverse()
print(liste1)

# index(elemanlari aramamizi sagliyor)
print(liste.index(29))

# count(listede o elemandan kac tane oldugunu bulmamiza yariyor)
sayi = [1, 4, 1, 6, 5, 2, 1, 3]
print(sayi.count(1))

# copy(bi listeden kopyalamaya yariyor)
harf = ["d", "g", "u", "w"]
harf1 = []
harf1 = harf.copy()

print(harf1)

#clear(listeyi silmeye(bosaltmaya) yarar)
print(liste.clear())

# list(set() (if are used the same values multiple times using this method will remove the copies)
numbers = [1, 2, 3, 4, 2, 4, 5, 8, 3, 5, 6,]
unique_numbers = list(set(numbers))
print(unique_numbers)
