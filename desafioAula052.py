#(Desafio 52) Faça um programa que leia um número inteiro e diga se ele é ou não
# um número primo.

print(f'\033[1;30;43m{" Número Primo ":=^60}\033[m')
cont = 0
num = int(input('Digite um número: '))

for x in range(1, num+1):
    if num % x == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(x, end='')
if cont == 2:
    print(f'\033[m\nO número {num}, é um número primo!')
else:
    print(f'\033[m\nO número {num}, não é um número primo!\nFoi dividido {cont} vezes.')
