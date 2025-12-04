#Calcular cateto e hipotenusa!
from math import hypot
cat_o = float(input('Qual o valor de cateto oposto ? '))
cat_a = float(input('qual o valor do cateto adjacente ? '))
hip = hypot(cat_o,cat_a)
print(f'A hipotenusa vai medir {hip:.2f}')