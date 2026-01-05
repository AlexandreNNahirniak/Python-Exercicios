dist = float(input('Qual a distância da viagem ? '))
print(f'Você esta prestes a começar a sua viagem de {dist:.1f}km')
if dist <=200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print(f'O valor da sua viagem é de R${valor:.2f}')