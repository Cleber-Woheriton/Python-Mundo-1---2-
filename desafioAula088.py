#(Desafio 88) Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites. O programa vai perguntar quantos jogos serão gerados e vai
# sortear 6 números entre 1 - 60 para cada jogo, cadastrando tudo em uma
# lista composta.
from random import randint
from time import sleep
print(f'\033[1;30;43m{" Programa da MEGA SENA ":=^60}\033[m')
cont = 0
jogo = []
contJogo = int(input('Quantos jogos quer que eu sorteie? '))
print(f'{" Sorteando ":=>25}{contJogo}{" Jogos ":=<25}')
for c in range(contJogo):
    for num in range(0, 6):
        sorteio = randint(1, 60)
        while sorteio in jogo:
            sorteio = randint(1, 60)
        else:
            jogo.append(sorteio)
        if len(jogo) == 6:
            cont += 1
            jogo.sort()
            print(f'Palpite do {cont}º jogo: {jogo}')
            sleep(2)
            jogo.clear()
print(f'{" Boa Sorte! ":=^50}')
