#(Desafio 86) Crie um programa que crie uma matriz de dimensão 3x3 e preencha
# com valores lidos pelo teclado. No final mostre a matriz na tela, com a formação
print(f'\033[1;30;43m{" Matriz (3x3) com Valores ":=^60}\033[m')
val = [[], [], []]
cont = cont1 = 0
for c in range(0, 9):
    val[cont1].append(int(input(f'Informe o valor da posição [{cont1}, {cont}]: ')))
    cont += 1
    if cont == 3:
        cont = 0
        cont1 += 1
cont1 = cont = 0
vog = 'a'
for c in range(0, 9):
    print(f'{vog}.{cont}=[  \033[35m{val[cont1][cont]:^5}\033[m  ]', end=' ')
    cont += 1
    if cont == 3:
        cont = 0
        cont1 += 1
        print('\t')
    if cont1 == 1:
        vog = 'b'
    if cont1 == 2:
        vog = 'c'
