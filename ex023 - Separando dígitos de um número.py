n001 = int(input('Digite um número: '))
U = n001//1%10
d = n001//10%10
c = n001//100%10
m = n001//1000%10
print(f'Analisando o número {n001}...')
print(f'Unidade: {U}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar {m}')