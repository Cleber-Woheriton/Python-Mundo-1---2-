#(Desafio 49) Refaça o desafio 09, mostrando a tabuada que o usuário escolher,
# ultilizando o for.

print(f'\033[1;30;43m{" Escolha a Tabuada ":=^70}\033[m')

fator1 = int(input('Escolha a tabuada.\nValor: '))

for fator2 in range(1, 11):
    produto = fator1 * fator2
    print(f'\033[7m{fator1} x {fator2:2} = {produto:2}\033[m')

#################### Solução do Curso ########################

for c in range(1, 11):
    print(f'{fator1} x {c :2} = {fator1* c}')