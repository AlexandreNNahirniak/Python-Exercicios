from random import randint
from time import sleep
cpu = randint(0, 5) # Faz o computador "pensar"
print('-=-' * 20)
print ('Vou pensar em um número entre 0 a 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == cpu:
    print('Parabéns, você ganhou!!!')
else:
    print(f'Eu ganhei, eu pensei no número {cpu} e não no número {jogador}!')