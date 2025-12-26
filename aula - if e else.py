'''tempo = int(input('Quantos anos tem seu carro ? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro antigo')
print('--FIM--')

#E também...
tempo = int(input('Quantos anos tem seu carro ? '))
print('Carro novo' if tempo <=3 else 'Carro antigo')
print('--FIM--')'''

'''#Outro teste
nome = str(input('Qual o seu nome ? '))
if nome == 'Alexandre':
    print(f'Seja bem-vindo de volta {nome}')
else:
    print(f'Olá, seja bem-vindo {nome}')
print('Bom dia!')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2
print(f'A sua média de notas foi {m}')
if m >= 6:
    print('Aprovado, Parabéns')
else:
    print('Reprovado, estude mais!')