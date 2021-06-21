#(Desafio 55) Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.

print(f'\033[1;30;43m{" Maior / Menor Peso do Grupo ":=^60}\033[m')

peso = [[], [], [], [], []]
for x in range(0, 5):
    peso[x] = float(input(f'Informe o {x + 1}º peso em Kg: '))

    if x == 4:
        print(f'O maior peso do grupo é: {max(peso)}Kg\nO menos peso do grupo é: {min(peso)}Kg')
