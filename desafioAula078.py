#(Desafio 78) Faça um progama que leia 5 valores numéricos e guarde em uma lista.
# No final mostre qual foi o maior e menor valor, e suas posições na lista.

print(f'\033[1;30;43m{" Adicionando 5 valores em uma lista ":=^70}\033[m')
val = []
minimo = maximo = 0
for c in range(0, 5):
    val.append(int(input('Digite um valor: ')))
print(f'O menor valor digitado é {min(val)}, e o maior valor digitado é {max(val)}')
minimo = int(min(val))
maximo = int(max(val))
print(f'O valor mínimo: ({minimo}). Está na posição: ', end='')
for c in range(len(val)):
    if val[c] == minimo:
        print(f'[\033[35m{c}\033[m]', end='')
print(f'\nO valor máximo: ({maximo}). Está na posição: ', end='')
for c in range(len(val)):
    if val[c] == maximo:
        print(f'[\033[35m{c}\033[m]', end='')

