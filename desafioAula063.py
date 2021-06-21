#(Desafio 63) Escreva um programa que leia um número n inteiro qualquer e mostre
# na tela os n primeiros elementos de uma sequência de fibonacci.
# Ex 0→ 1→ 1→ 2→ 3→ 5→ 8→

print(f'\033[1;30;43m{" Sequência de Fibonacci ":=^60}\033[m')
valA = f = 0
valB = valC = cont = 1
print('Quantos números de sequência deseja ver?')
nFb = int(input('Valor: '))

while valC != 0:
    while cont <= nFb:
        print(f'\033[33m{valA}\033[m', end='\033[31m→ \033[m')
        if cont < nFb:
            print(f'\033[33m{valB}\033[m', end='\033[31m→ \033[m')
            valA += valB
            valB += valA
            cont += 1
        cont += 1
    print('\nQuantos mais deseja ver?')
    valC = int(input('Valor: '))
    nFb += valC


print(f'\033[35m{" Obrigado por usar nosso sistema! ":~^60}\033[m')
