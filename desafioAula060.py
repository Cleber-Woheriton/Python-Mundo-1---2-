#(Desafio 60) Faça um programa que leia um número qualquer e mostre o seu
# fatorial. Ex 5! = 5x4x3x2x1 = 120
import time
print(f'\033[1;30;43m{" Fatorial de um Número ":=^70}\033[m')

num = int(input('Escolha um número: '))
num1 = 1
while num >= 1:
    time.sleep(1)
    print(f'{num} x ', end='')
    num1 *= num
    num -= 1
print('= ', end='')
time.sleep(1)
print(f'\033[34m{num1}\033[m')
# Solução do curso
"""import math import factorial
    n = int(input('Digite um número: '))
    f = factorial(n)
    print('O fatorial de {} é {}'.format(n, f)"""
