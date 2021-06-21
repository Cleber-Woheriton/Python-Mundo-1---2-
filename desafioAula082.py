# (Desafio 82) Crie um programa que irá armazenar vários números em uma lista.
# Depois disso crie duas listas exatas que vão conter apenas valores pares e os valores
# ímpares digitados, respectivamente. Ao final mostre o conteúdo das três listas geradas.
print(f'\033[1;30;43m{" Lista com par e uma com ímpar ":=^70}\033[m')
continuar = 'sim'
numeros = []
numpar = []
numimp = []
while continuar in 'sim':
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [sim/não]: ')).strip().lower()
for c in range(len(numeros)):
    if numeros[c] % 2 == 0:
        numpar.append(numeros[:][c])
    else:
        numimp.append(numeros[:][c])
print(f'Valor(es) digitado(s): \033[35m{numeros}\033[m')
if len(numpar) >= 1:
    print(f'Valor par: \033[35m{numpar}\033[m')
else:
    print('Não possuí valor par!')
if len(numimp) >= 1:
    print(f'Valor ímpar: \033[35m{numimp}\033[m')
else:
    print('Não possuí valor ímpar!')
