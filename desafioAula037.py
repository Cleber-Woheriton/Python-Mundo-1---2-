#(Desafio 37) Escreva um programa que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão
# Decimal, octal, hexadecimal
print('=-'*10, '\033[30;43mBináxio, Octal e Hexadecimal\033[m', '=-'*10)
numero = int(input('Digite um número positivo qualquer: '))
if numero < 0:
    print('Valor negativo não é aceitável!')

print('\033[30;43m(1) para tranformar em Binário    \033[m'
      '\n\033[30;43m(2) para transformar em Octal     \033[m'
      '\n\033[30;43m(3) para tranformar em Hexadecimal\033[m')
opc = int(input('Opção escolhida: '))
if opc < 1 or opc >= 4:
    print('Opção não disponível!')
elif opc == 1:
    print(f'O número {numero} em binário é, {bin(numero)[2:]}')# função para binário
elif opc == 2:
    print(f'O número {numero} em octal é, {oct(numero)[2:]}')# função octal
else:
    print(f'O número {numero} em hexadecimal é, {hex(numero)[2:]}')# função hexadecimal
    print('Tabela Hexadecimal:\nA = 10 | B = 11\nC = 12 | D = 13\nE = 14 | F = 15')
