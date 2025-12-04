from math import sin, cos, radians, tan
ângulo = float(input('Qual ângulo você deseja ? '))
seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem o TANGENTE de {tangente:.2f}')