#(Desafio 32) Faça um programa que leia qualquer
# ano e informe se ele  é bissexto.

print('*-'*15, 'Ano Bissexto', '*-'*15)

ano = int(input('Informe o ano: '))

if ano % 4 == 0:# Todo ano que dividido por 4 tem resto 0 é bissexto.
    print(f'Ano de {ano}, é um ano bissexto!')
else:
    print(f'O ano de {ano}, não é um ano bissexto!')