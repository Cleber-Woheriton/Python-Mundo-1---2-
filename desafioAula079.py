#(Desafio 79) Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista na lista, ele não será
# adicionado . No final serão exibidos todos os valores, válidos digitados em ordem crescente.
print(f'\033[1;30;43m{" Adicionar números únicos em lista ":=^60}\033[m')
numeros = []
continuar = 'sim'
cont = val = 0
while continuar in 'sim':
    val = int(input('Digite um valor: '))
    if val not in numeros:
        numeros.append(val)
    else:
        print('O número já foi adicionado na lista!')
    continuar = str(input('Deseja continuar?: ')).strip().lower()
    cont += 1
numeros.sort()
print(f'Você digitou um total de {cont} números!\nOs registrados foram \033[35m{numeros}\033[m')
