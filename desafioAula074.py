# (Desafio 74) Crie um programa que vai gerar cinco números aleatórios e
# colocar em uma tupla. Depos disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.
from random import randint

print(f'\033[1;30;43m{" Números Aleatórios ":=^70}\033[m')
numesc = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))
print(f'\033[1;30;43m{" Números Aleatório Escolhidos ":=^70}\033[m')
for c in range(0, 5):
    print(numesc[c], end='/ ')
#print(f'{numesc[0: 5]}')
print(f'\n\033[1;30;43m{" Maior Número ":=^70}\033[m')
print(max(numesc))
print(f'\033[1;30;43m{" Menor Número ":=^70}\033[m')
print(min(numesc))
