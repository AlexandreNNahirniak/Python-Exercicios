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

#Outro teste
nome = str(input('Qual o seu nome ? '))
if nome == 'Alexandre':
    print(f'Seja bem-vindo de volta {nome}')
else:
    print(f'Olá, seja bem-vindo {nome}')
print('Bom dia!')