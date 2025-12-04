#Teste 001
nome=input('Qual o seu nome ? ')
print(f'Seja muito bem-vindo {nome}, sinta-se a vontade!')


#Teste 002
input('Vou te fazer algumas perguntas sobre a sua data de nascimento, responda essas perguntas em números, ok ? ')
dia=int(input('Em que dia você nasceu ? '))
mês=int(input('Em que mês ? '))
ano=int(input('Em que ano ? '))
input(f'Você nasceu no dia {dia} do {mês} de {ano}, certo ? ')
print('Obrigado por confirmar... Agora vamos trabalhar com contas!')


#Teste 003
n001=int(input('Digite um número aleatório: '))
n002=int(input('Agora digie outro: '))
soma=n001+n002
subtração=n001-n002
multiplicação=n001*n002
divisão=n001/n002
print(f'A soma de {n001} com {n002} tem o resultado de {soma}')
print(f'A subtração de {n001} com {n002} tem o resultado de {subtração}')
print(f'A multiplicação de {n001} com {n002} tem o resultado de {multiplicação}')
print(f'A divisão de {n001} com {n002} tem o resultado de {divisão}')


#Teste 004
input('Agora vamos trabalhar com análise de de palavras, ok ? ')
algo_1=input('Digite algo aleatório: ')
input(f'Você digitou {algo_1}, correto ? ')
input('Vamos analisar o que foi escrito ?? ')
print(f'O tipo primitivo de {algo_1} é:',type(algo_1))
print('É um número ? ',algo_1.isnumeric())
print('É alfabético ? ',algo_1.isalpha())
print('É alfanumérico ? ',algo_1.isalnum())
print('Só tem espaço ? ',algo_1.isspace())
print('Está em maiúsculo ? ',algo_1.isupper())
print('Está em minúsculo ? ',algo_1.islower())
print('É capitalizada ? ',algo_1.istitle())
