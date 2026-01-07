salário = float(input('Qual o seu salário ? R$'))
if salário <= 1250:
    novo = (salário * 15 / 100) + salário
else:
    novo = (salário * 10 / 100) + salário
print(f'Quem ganhava R${salário:.2f} agora passa a ganhar R${novo:.2f} agora!')