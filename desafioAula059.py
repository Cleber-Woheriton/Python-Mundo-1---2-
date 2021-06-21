#(Desafio 59) Crie um programa que leia dois valores e mostre um menu na tela:
#[1]Somar\ [2]Multiplicar\ [3]Maior valor\ [4]Novos Números\ [5]Sair. Realizar as operações
from time import sleep

print(f'\033[1;30;43m{" Sistem de Menu ":=^70}\033[m')
valor = 0
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
opc = 0

while opc == 0:
    print(f'\033[33m{" Escolha uma opção ":=^80}\033[m')
    print('\033[32m[1]\033[m Somar\n\033[32m[2]\033[m Multiplicar\n'
          '\033[32m[3]\033[m Qual é o maior valor\n'
          '\033[32m[4]\033[m Digitar nonamente\n\033[32m[5]\033[m Sair')
    opc = int(input('Opção: '))
    if opc == 1:
        valor = (n1 + n2)
        print(f'{n1} + {n2} = {valor}')
        sleep(2)

    elif opc == 2:
        valor = (n1 * n2)
        print(f'{n1} x {n2} = {valor}')
        sleep(2)

    elif opc == 3:
        if n1 > n2:
            valor = n1
            print(f'O maior valor entre ({n1} e {n2}) = {valor}')
            sleep(2)

        elif n2 > n1:
            valor = n2
            print(f'O maior valor entre ({n1} e {n2}) = {valor}')
            sleep(2)

        else:
            print(f'Valores iguais! ({n1} e {n2})')
            sleep(2)

    elif opc == 4:
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))

    elif opc == 5:
        print(f'\033[1;30;43m{" Obrigado por usar nosso sistema. ":~^70}\033[m')
        sleep(2)
        exit()
    else:
        print('\033[31mOpção inválida!\033[m\nTente novamente.')
        sleep(2)
    opc = 0

