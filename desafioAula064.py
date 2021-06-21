#(Desafio 64) Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o valor 999).
import time
print(f'\033[1;30;43m{" Soma de N, Números ":=^60}\033[m')

n = cont = val = 0
print('Caso queira sair digite "999" ')
while n != 999:
    val += n
    n = int(input('Informe um número inteiro: '))
    cont += 1
print(f'{"Calculando...."}')
time.sleep(2)
print(f'A soma de todos os números é {val}.\nE você digitou um total de {cont - 1} números')