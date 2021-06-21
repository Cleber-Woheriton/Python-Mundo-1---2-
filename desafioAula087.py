#(Desafio 87) Aprimore o desafio anterior, mostrando no final. A) A soma de todos
# os valores pares. B) A soma dos valores da 3º coluna. C) O maior valor da 2º linha.
print(f'\033[1;30;43m{" Calculando Valor da Matriz ":=^60}\033[m')
matriz = [[], [], []]
valor = cont = cont1 = par = coluna = 0
for c in range(0, 9):
    valor = int(input(f'Informe o valor da posição [{cont1}, {cont}]: '))
    if valor % 2 == 0:
        par += valor
    matriz[cont1].append(valor)
    cont += 1
    if cont == 3:
        coluna += valor
        cont = 0
        cont1 += 1
    if cont1 == 3 and cont == 0:
        cont = cont1 = 0
print(f'{" Matriz ":=^50}')
for c in range(0, 9):
    print(f'[\033[30;46m{matriz[cont1][cont]:^5}\033[m]', end='')
    cont += 1
    if cont == 3:
        cont = 0
        cont1 += 1
        print('\t')
print(f'{" Resultados ":=^50}'
      f'\nA soma dos valores pares: {par}\nA soma da terceira coluna: {coluna}'
      f'\nO maior valor da 2º coluna: {max(matriz[1])}')
