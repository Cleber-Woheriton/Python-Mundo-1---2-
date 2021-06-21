#(Desafio 45) Crie um programa que faça o computador joguar Jokenpô com você.
from random import randint
import time

print('-='*10, '\033[30;43mJokenpô VS PC\033[m', '=-'*10)

escolhaPC = ['Pedra', 'Papel', 'Tesoura']
pessoa = int(input('Faça sua escolha\n 1- Pedra\n 2- Papel\n 3- Tesoura\n Responda: '))
x = randint(0, 2)
escolhaPC[0] = escolhaPC[x]
print('\033[33mJooo....\033[m')
time.sleep(1)
print('\033[33mkenn....\033[m')
time.sleep(1)
print('\033[33mPôôô....\033[m')

if pessoa == 1:
    pessoa = 'Pedra'
elif pessoa == 2:
    pessoa = 'Papel'
elif pessoa == 3:
    pessoa = 'Tesoura'
else:
    print('\033[1;41mOpss...        \033[m\n\033[1;41mOpção Inválida!\033[m')
    exit()

if pessoa in escolhaPC[0]:
    print('\033[1;43mEmpate!\033[m')
elif 'Pedra' in pessoa and 'Papel' in escolhaPC[0]:
    print('\033[31mVocê perdeu, Papel vence Pedra!\033[m')
elif 'Pedra' in pessoa and 'Tesoura' in escolhaPC[0]:
    print('\033[32mVocê Venceu, Pedra vence Tesoura!\033[m')
elif 'Tesoura' in pessoa and 'Papel' in escolhaPC[0]:
    print('\033[32mVocê Venceu! Tesoura vence Papel\033[m')
elif 'Tesoura' in pessoa and 'Pedra' in escolhaPC[0]:
    print('\033[31mVocê Perdeu! Pedra vence Tesoura.\033[m')
elif 'Papel' in pessoa and 'Pedra' in escolhaPC[0]:
    print('\033[32mVocê Venceu! Papel vence Pedra.\033[m')
elif 'Papel' in pessoa and 'Tesoura' in escolhaPC[0]:
    print('\033[31mVocê Perdeu! Tesoura vence Papel.\033[m')
print(f'\033[34mVocê : {pessoa}\nMáquina: {escolhaPC[0]}\033[m')
