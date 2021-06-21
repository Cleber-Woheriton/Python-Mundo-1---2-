#(Desafio 61) Refaça o desafio 51, lendo o primeiro termo e a razão de uma P.A
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print(f'\033[1;30;43m{" Razão da P.A (Usando while) ":=^60}\033[m')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = termo + ((10 - 1) * razao)

while termo <= decimo:
    valor = termo
    print(valor, end='→ ')
    termo += razao
print('Fim!')
# Solução do Curso
"""primeiro = int(input('Priemiro termo:'))
   razão = int(input('Razão da PA: '))
   
   cont = 1
   while cont <= 10:
        print('{} →'.format(termo), end='')
        termo += razão
        cont += 1
print('Fim!')"""