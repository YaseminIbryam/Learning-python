sayi=int(input("Bir sayi girin:"))
prime = True #prime number = asal sayi = просто число  
for i in range(2,sayi):
    if sayi%i == 0:
        prime=False
        break
if prime==True:
    print(f"{sayi} asal bir sayi")
else: 
    print(f"{sayi} asal bir sayi degil")
        
        
        
