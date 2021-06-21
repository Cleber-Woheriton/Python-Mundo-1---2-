#(Desafio 66) Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar 999, que é a condiçaõ de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre elas.
# (Desconsiderando o 999).

print(f'\033[1;30;43m{" Soma de N números ":~^70}\033[m')
n = cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram informados um total de {cont} números,\ne a soma entre elas é {soma}')