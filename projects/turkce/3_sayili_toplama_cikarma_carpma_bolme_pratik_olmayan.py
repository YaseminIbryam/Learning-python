a=int(input("sayi"))
b=int(input("sayi"))
c=int(input("sayi"))
d=(a+b)
e=(a-b)
f=(a*b)
g=(a/b)
secenek=int(input("1-topla/n2-cikar/n3-carp/n4-bol"))
if secenek ==1:
 print(a+b)
 secenek=int(input("1-topla/n2-cikar/n3-carp/n4-bol"))
 if secenek ==1:
  print(d+c)
 elif secenek ==2:
    print(d-c)
 elif secenek ==3:
    print(d*c)
 elif secenek ==4:
    print(d/c)
elif secenek ==2:
 print (a-b)
 secenek=int(input("1-topla/n2-cikar/n3-carp/n4-bol"))
 if secenek ==1:
  print(e+c)
 elif secenek ==2:
    print(e-c)
 elif secenek ==3:
   print(e*c)
 elif secenek ==4:
    print(e/c)
elif secenek ==3:
 print (a*b)
 secenek=int(input("1-topla/n2-cikar/n3-carp/n4-bol"))
 if secenek ==1:
  print(f+c)
 elif secenek ==2:
    print(f-c)
 elif secenek ==3:
   print(f*c)
 elif secenek ==4:
    print(f/c)
else:
 print (a/b)
 secenek=int(input("1-topla/n2-cikar/n3-carp/n4-bol"))
 if secenek ==1:
  print(g+c)
 elif secenek ==2:
    print(g-c)
 elif secenek ==3:
   print(g*c)
 elif secenek ==4:
    print(g/c)

