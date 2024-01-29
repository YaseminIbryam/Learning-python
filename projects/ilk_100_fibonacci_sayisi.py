fibonacci_sayilar=[]
while len(fibonacci_sayilar) < 100:
    a=1
    b=1
    c=a+b
    fibonacci_sayilar.append(a)
    fibonacci_sayilar.append(b)
    fibonacci_sayilar.append(c)
    while len(fibonacci_sayilar) <= 100:
        a=b+c
        b=c+a 
        c=a+b
        if len(fibonacci_sayilar) < 100:
            fibonacci_sayilar.append(a)
            if len(fibonacci_sayilar) < 100:
                fibonacci_sayilar.append(b)
                if len(fibonacci_sayilar) < 100:
                    fibonacci_sayilar.append(c)
        else: 
            break
print(fibonacci_sayilar)
