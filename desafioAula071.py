# (Desafio 71) Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
# programa deve informar quais notas serão entregues. Obs;
# Considerando que possua cédulas de R$ 50, 20, 10, 1.
from time import sleep

print(f'\033[1;30;43m{" Banco Eletônico Calebe ":=^70}\033[m')
print('Por favor insira seu cartão..')
sleep(1)
print('\033[33mAguarde...\033[m')
sleep(2)
senha = 0
senha = int(input('Digite a senha: '))
print('\033[34mProcessando...\033[m')
sleep(2)
operação = saldo = saque = deposito = totalCed = valor = 0
cédula = 50
while True:
    print(f'\033[7m{" Escolha a Operação ":=^70}\033[m')
    print('1- Extrato     2- Saque\n3- Depósito    4- Sair')
    operação = int(input('Informe a opção desejada: '))
    if operação <= 0:
        print('Operação Inválida!')
        sleep(2)
    if operação >= 5:
        print('Operação Inválida!')
        sleep(2)
    if operação == 1:
        print(f'Saldo R$: {saldo}')
        sleep(2)
    if operação == 2:
        print('Valor a sacar?')
        saque = int(input('R$: '))
        valor = saque
        if valor <= saldo:
            while True:
                if valor >= cédula:
                    valor -= cédula
                    totalCed += 1
                else:
                    if totalCed > 0:
                        print(f'Total de {totalCed} cédulas de R$: {cédula}')
                    elif cédula == 50:
                        cédula = 20
                    elif cédula == 20:
                        cédula = 10
                    elif cédula == 10:
                        cédula = 1
                    elif totalCed == 0:
                        print('\033[34mTransação Concluida!\033[m')
                        saldo -= saque
                        sleep(2)
                        cédula = 50
                        break
                    totalCed = 0
        else:
            print(f'Saldo negativo!\nR$: \033[31m{saldo}\033[m')
            sleep(2)
    if operação == 3:
        print('Valor a depositar?')
        deposito = int(input('R$: '))
        saldo += deposito
        sleep(2)
    if operação == 4:
        print('Obrigado por usar nosso sistema.\nVolte sempre!')
        sleep(2)
        break
