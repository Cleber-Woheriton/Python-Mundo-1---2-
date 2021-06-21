# (Desafio 58) Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
# número entre 0 e 10. Só que agora o jogador tentar adivinhar até acertar, mostrando
# no final mostre quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
print(f'\033[1;30;43m{" Desafio 28 Melhorado - Adivinhe o Número ":=^70}\033[m')
num = randint(0, 10)
print('Acabei de pensar em um número, consegue advinhar? ^^')
adv = int(input('Palpite de [0 a 10]: '))
cont = 1

while adv != num:
    sleep(2)
    print(f'\033[35m{"":~^80}\033[m')
    while adv < 0:
        print('Só é valido números entre 0 e 10!\n Tente novamente.')
        adv = int(input('Digite sua escolha: '))
    while adv > 10:
        print('Só é valido números entre 0 e 10!\n Tente novamente.')
        adv = int(input('Digite sua escolha: '))
    cont += 1
    if adv < num:
        print('Errou!\nO palpite que escolheu é\033[33m menor\033[m que o número que pensei.')
        adv = int(input('Tente novamente, qual será seu palpite: '))
    elif adv > num:
        print('Errou!\nO palpite que escolheu é\033[33m maior\033[m que o número que pensei.')
        adv = int(input('Tente novamente, qual  será seu palpite: '))
print(f'\033[32mParabéns, Você Ganhou!!\033[m\nUsou {cont} números de tentativa(s) válidas! ')
