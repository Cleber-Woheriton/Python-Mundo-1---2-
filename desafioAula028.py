import random # Para usar o randomico é preciso fazer o import
from time import sleep # Deixar com efeito de pensando sleep()
# (Desafio 28) Escreva um programa que faça o computador "Pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.


def sortear(adv, num): # Defini um método para verificar o número sorteado
    print('Processando...')
    sleep(3)
    if adv == num:
        print(f'\033[32mParabéns, você acertou!!! O número sorteado foi {num}.')
    else:
        print(f'\033[33mVocê errou, boa sorte na proxima!! O número sorteado foi {num}.')


num = random.randint(0, 5)# Atribuindo um valor randômico entre 0 e 5 atribuindo
                          # ao num.

adv = int(input('Adivinhe o número sorteado de 0 a 5: '))
# if para verificar se o número do usuário é válido!
if adv < 0:
    print('\033[31mNúmero negativo não é correto para o sorteio!')
elif adv > 5:
    print('\033[31mLimite ultrapassado, o máximo é o valor (5)')
else:
    sortear(adv, num)# Instanciando para o def enviando os valores!