preço = float(input('Qual o preço do produto ? R$'))
desc = preço-(preço*5/100)
print(f'O produto que custava R${preço:.2f}, após o desconto de 5% vai custar R${desc:.2f}')