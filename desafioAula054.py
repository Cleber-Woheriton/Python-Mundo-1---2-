#(Desafio 54) Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já estão maiores.
from datetime import date
print(f'\033[1;30;43m{" Gupo de Maior e Menor Idade ":=^70}\033[m')
maior = 0
menor = 0
ano = ''
atual = date.today().year
for x in range(0, 7):
    ano = int(input(f'Digite o ano do {x + 1}º integrante: '))
    if (atual - ano) >= 21:
        maior += 1
    else:
        menor += 1
print(f'Este grupo tem.\n{maior} Maior(es) de idade.\n{menor} Menor(es) de idade.')

