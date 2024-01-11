import math

# toplama(+)
# cikarma(-)
# carpma(*)
# bolme(/)
# tam bolme(//)
# kuvvet alma, степен(**)
# kare kok,√(math.sqrt)
# mutlak deger, модул(abs)

# yuvarlama, закръгляне(round) #round(sayi, virgulden sonra kacinci sayiya yuvarlansin)
print(round(4.6198, 2))

# mod alma(%) #boldukten sonraki kalan sayi
print(8 % 3)  # 8/3=6 kalan 2

# "{:.2f}".format(sayi) veya f"{sayi:.2f}" bir sayinin noktadan sonraki 2 hanesi gösteriliyor
# ve sayiyi yuvarlamaya yariyor
print(f"{5385:.2f}")
print("{:.4f}".format(3.53875385))

# bir sayinin onunde baska bir sayi bulunmasini sagliyor
# ornek olarak saniyeler ile baslamasi gerekiyorsa ve 2 sayidan olusmasi gerekiyor ve bazen 0 ile baslamasi gerekirse
seconds = 8
print(f"{seconds:02d}")

# Trigonometric functions
angle_in_degrees = 45
angle_in_radians = math.radians(angle_in_degrees)
sin_result = math.sin(angle_in_radians)
cos_result = math.cos(angle_in_radians)
tan_result = math.tan(angle_in_radians)

# Logarithm
num = 8
result_logarithm = math.log2(num)
print(f"Logarithm (base 2) of {num}: {result_logarithm}")

# factorial
n = 5
print(math.factorial(n))