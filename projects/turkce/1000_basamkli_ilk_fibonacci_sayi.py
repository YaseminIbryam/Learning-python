fibonacci_sayi=[1,1]
index=2
while len(str(fibonacci_sayi[-1]))<=1000:
    fibonacci_sayi.append(fibonacci_sayi[index - 2] + (fibonacci_sayi[index - 1]))
    index+=1
    if len(str(fibonacci_sayi[-1]))==1000:
        
        print(str(fibonacci_sayi[-1]))
        break
