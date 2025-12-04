#Selecionando item da lista de modo aleatório!
import random
nome001 = input('Primeiro aluno: ')
nome002 = input('Segundo aluno: ')
nome003 = input('Terceiro aluno: ')
nome004 = input('Quarto aluno: ')
lista = [nome001, nome002, nome003, nome004]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')

# E também
from random import choice
nome001 = input('Primeiro aluno: ')
nome002 = input('Segundo aluno: ')
nome003 = input('Terceiro aluno: ')
nome004 = input('Quarto aluno: ')
lista = [nome001, nome002, nome003, nome004]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')
