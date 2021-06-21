#(Desafio 85) Crie um programa que leia sete valores numéricos e cadastre-os
# em uma lista única que mantenha separado os valores pares e impares. No final
# mostre os valores pares e impares em ordem crescente.
print(f'\033[1;43;30m{" Cadastrar Valores ":=^60}\033[m')

num = [[], []]
val = 0
for c in range(0, 7):
    val = (int(input(f'{c+1}º valor: ')))
    if val % 2 == 0:
        num[0].append(val) # Valores pares
    else:
        num[1].append(val) # Valores ímpares
num[0].sort()
num[1].sort()
print(f'Os valores pares foram: {num[0]}\nOs valores ímpares foram: {num[1]}')
