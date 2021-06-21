#(Desafio 33) Faça um programa que leia 3 números e mostre
# qual é o maior e qual é o menor.

print('*-'*15, 'Número Maior e Menor', '*-'*15)
num = [[], [], []]

for x in range(0, 3):
    n = x+1
    num[x] = int(input(f'Digite o {n}º número: '))

    if x == 2:
        print('-'*30)
        print(f'Maior valor digitado {max(num)}')
        print(f'Menor valor digitado: {min(num)}')