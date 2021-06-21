#(Desafio 70) Crie um programa que leia o nome e o preço de vários produtos.
# O programa deve  perguntar se ele deseja continuar comprando. No final mostre;
#{A)Total gasto na compra. B)Quantos produtos custam mais de 1000. C)Nome do produto
# mais barato.}
from time import sleep
print(f'\033[1;30;43m{" Loja Calebe Tec. ":=^70}\033[m')

nome = res = nomeB = ''
preço = total = prod = prodMil = 0
print(f'{" Nota Fiscal Loj. Calebe Tec. ":~^60}')
nome = str(input('Nome do produto: ')).title()
preço = float(input('Valor do produto: '))
prod = preço
nomeB = nome
while True:
    if preço < prod:
        prod = preço
        nomeB = nome
    total += preço
    if preço > 1000:
        prodMil += 1
    res = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    while res not in 'sn':
        res = str(input('Continuar comprando? [S/N]: ')).strip().lower()[0]
    if res in 'n':
        print('\033[34mProcessando...\033[m')
        sleep(1)
        print(f'Total da compra R$:\033[32m{total:.3f}\033[m'
              f'\nQuantidade de produtos com valor acima de 1000 (\033[32m{prodMil}\033[m)'
              f'\nNome do produto mais barato \033[32m{nomeB}\033[m')
        sleep(10)
        print('Obrigado por usar nosso sistema!')
        sleep(5)
        break
    nome = str(input('Nome do produto: ')).title()
    preço = float(input('Valor do produto: '))
