#(Desafio 81) Crie um programa que irá ler vários números e colocar em uma lista.
# Despois disso mostre A) Quantos números foram digitados. B) A lista de valores ordenados
# de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
print(f'\033[1;30;43m{" Lista de Números ":=^70}\033[m')
continuar = 'sim'
numeros = []
cont = 0
while continuar in 'sim':
    cont += 1
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [sim/não]: ')).strip().lower()
numeros.sort(reverse=True)
print(f'Você digitou {cont} valor(es).\nOs números digitados foram {numeros}')
if 5 in numeros:
    print('Possuí o valor 5!')
else:
    print('Não possuí o valor 5!')

