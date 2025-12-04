#Parte 1
nome=input('Qual o seu nome ? ')
print(f'Olá, seja bem-vindo {nome}, vamos treinar')
input('Vou perguntar algumas informações sobre você, ok ? ')
dia=input('Em que dia você nasceu ? ')
mês=input('Em que mês ? (responda em número por favor):')
ano=input('Em que ano ? ')
input(f'Você nasceu no dia {dia} de {mês} de {ano}, correto ? ')

#Parte 2
input('Agora vamos para conversão de dinheiro, pressione enter para continuar')
carteira=float(input('Quantos reais você tem atualmente ? R$'))
comp_dolar=carteira/5.25
print(f'Atualmente com R${carteira:.2f} você pode comprar U${comp_dolar:.2f}')

#Parte 3
input('Vamos converter a temperatura ? ')
temp_c=float(input('Qual a temperatura atual ? '))
temp_f=((9*temp_c)/5)+32
print(f'Atualmente a temperatura em C esta em {temp_c:.1f}ºC e em F está em {temp_f:.1f}ºF')

#Parte 4
input(f'Vamos fazer cálculo com porcentagem ok {nome}, (Rendimento em CDB ao mês aproximadamente ok ? ')
carteira2=float(input('Quantos reais você tem em banco neste momento ? '))
CDB=carteira2*0.8/100
rendimento=carteira2+CDB
print(f'Se você colocar {carteira2} para render, você vai ter aproximadamente {carteira2+CDB:.2f} em redimento em 30 dias!')