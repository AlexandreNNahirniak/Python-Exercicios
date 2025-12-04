dias = int(input('Quantos dias o carro ficou alugado ? '))
km = float(input('Quantos km foram rodados ? '))
total = (dias * 75) + (km*0.30)
print(f'O valor a ser pago pelo aluguel é de: {total:.2f}')