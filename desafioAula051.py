#(Desafio 51) Desenvolva um programa que leia o primeiro termo e a razão de uma P.A
# no final mostre os 10 primeiros termo dessa progressão.

print(f'\033[1;30;43m{" 10 Termos de uma PA ":=^60}\033[m')

prTer = int(input('Informe o primeiro termo: '))
rzão = int(input('Informe a razão: '))
decimo = prTer + (10 - 1) * rzão

for x in range(prTer, decimo + rzão, rzão):
    print(f'{x}', end='→ ')
print('Fim!')
