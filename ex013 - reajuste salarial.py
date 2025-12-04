sal_ant=float(input('Qual o salário do funcionário ? '))
porc=sal_ant*15/100
novo_sal=sal_ant+porc
print(f'Após o aumento de 15% ser aplicado sobre o salário de R${sal_ant:.2f}, o novo salário vai ser de R${novo_sal:.2f}')