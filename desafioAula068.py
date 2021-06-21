#(Desafio 68) Faça um programa que jogue Par ou Impar com o Comp. O jogo só será
# interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
from random import randint
from time import sleep
print(f'\033[1;30;43m{" Par ou Impar... Goo!!! ":=^70}\033[m')
esc = ''
cont = num = 0
while True:
    escPC = randint(0, 10)
    esc = str(input('Par ou Impar [P\I]: ')).strip().lower()[0]
    num = int(input('Escolha um valor: '))
    if esc in 'pi':
        num += escPC
        print(f'{"=-"}' * 15)
        if esc in 'p':
            if num % 2 == 0:
                print(f'\033[32mVocê Ganhou!\033[35m\nVocê = ({num - escPC} / Par)\033[m'
                      f'\n\033[33mComputador = ({escPC} / Impar)\033[m\nTotal {num} = Par!')
                print(f'{"=-"}'*15)
                cont += 1
            else:
                print(f'\033[31mVocê Perdeu!!\033[35m\nVocê = ({num - escPC} / Par)'
                      f'\n\033[33mComputador = ({escPC} / Impar)\033[m\nTotal {num} = Impar!')
                print(f'{"=-"}' * 15)
                sleep(2)
                break
        if esc in 'i':
            if num % 2 != 0:
                print(f'\033[32mVocê Ganhou!\033[35m\nVocê = ({num - escPC} / Impar)'
                      f'\n\033[33mComputador = ({escPC} / Par)\033[m\nTotal {num} = Impar!')
                print(f'{"=-"}' * 15)
                cont += 1
            else:
                print(f'\033[31mVocê Perdeu!!\033[35m\nVocê = ({num - escPC} / Impar)'
                      f'\n\033[33mComputador = ({escPC} / Par)\033[m\nTotal {num} = Par!')
                print(f'{"=-"}' * 15)
                sleep(2)
                break
    else:
        print(f'{"":~^60}')
        print('Opção inválida!')
print(f'Você ganhou {cont} vez(es) consecutivas.\nFim do jogo.')
