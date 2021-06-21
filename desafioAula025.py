#(Desafio 25) Crie um programa que leia o nome de  uma pessoa e diga se ela
# possuí "Silva" no nome.
nome = str(input('Informe seu nome: '))
nome = nome.lower()

if 'silva' in nome:
    print('Possuí "Silva" no nome!')
else:
    print('Não possuí "Silva" no nome!')