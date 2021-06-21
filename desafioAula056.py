#(Desafio 56) Desenvolva um programa que leia o nome, idade e sexo de
# 4 pessoas. No final do programa mostre (A média de idade do grupo \
# Qual é o nome do homem mais velho \ Quantas mulheres tem menos de 20 anos.)

import time

print(f'\033[1;30;43m{" Resultado Geral do Grupo ":=^60}\033[m')

media = 0
maisVelho = 0
nomeVelho = ''
idad = [[], [], [], []]
mMenor = 0
for x in range(0, 4):
    print('*'*10, f' Informe o nome da {x+1}º pessoa 7', '*'*10)
    nome = str(input('Infome o nome: ')).strip()
    idad[x] = int(input('Infome a idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()

    print('Processando...')
    time.sleep(2)
    if x == 1 and sexo in 'm':
        nomeVelho = nome
        maisVelho = idad[x]
    if sexo == 'm' and idad[x] > maisVelho:
        maisVelho = idad[x]
        nomeVelho = nome
    if sexo == 'f' and idad[x] < 20:
        mMenor += 1

media = (sum(idad)) / 4

print(f'A média desse grupo é: {media}\nE o Homem mais velho tem {maisVelho}, e se '
      f'Chama {nomeVelho}\nE existe {mMenor}, mulher(es) com menos de 20 anos.')

