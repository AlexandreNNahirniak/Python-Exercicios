vel = float(input('Em que velocidade o veículo passou ? '))
if vel > 80:
    multa = (vel-80) * 7
    print(f'Você excedeu o limite de velocidade da via e foi multado... \n O valor da multa é de R${multa:.2f}! \n Por favor, dirija na velocidade adequeda da via e com segurança!')
print('Boa viagem e dirija com segurança!')