# (Desafio 80) Crie um programa ondeo usuário possa digitar cinco valores
# e cadastre-os em uma lista, já na posição correta da inserção, sem usar o sort()
# No final mostre a lista ordenada na tela.

print(f'\033[1;30;43m{" Adicione 5 números na Lista em Ordem ":=^70}\033[m')
numeros = []
c = 0
while c < 5:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        if c == 0 or num > numeros[-1]:
            numeros.append(num)
            c += 1
        else:
            pos = 0
            c += 1
            while pos < len(numeros):
                if num < numeros[pos]:
                    numeros.insert(pos, num)
                    break
                if num > numeros[pos]:
                    if num > numeros[pos + 1]:
                        numeros.insert(pos + 2, num)
                    else:
                        numeros.insert(pos + 1, num)
                    break
    else:
        print('O número já foi informado!')
print(numeros)
'''Solução do Guanabara!
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)
'''