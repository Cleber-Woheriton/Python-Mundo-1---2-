# (Desafio 50) Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares, se o valor for ímpar desconsidere-o.

print(f'\033[1;30;43m{" Soma dos Pares ":=^60}\033[m')
val = 0
cont = 0
for x in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        val += num
        cont += 1
print(f'Dos 6 números você informou {cont} são par(es).\nE a soma dos pares digitado foi: {val}')
