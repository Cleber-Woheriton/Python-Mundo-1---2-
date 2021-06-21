#(Desafio 47) Crie um programa que mostre na tela todos os números pares que estão
# no intervalo entre 1 e 50.

print(f'\033[1;30;43m{"números Pares de 0 - 50":=^50}\033[m')

for x in range(1, 51):
    if x % 2 == 0:
        print(x, end=' ')
############## Solução do curso

for c in range(2, 51, 2):
    print(c, end=' ')
