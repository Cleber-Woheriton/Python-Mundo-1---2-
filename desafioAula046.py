#(Desafio 46) Faça um programa que mostre na tela uma contagem regressiva para o
# estouro de fogos de artifício, de 10 até 0, com uma pausa de 1 segundo entre elas.
import time

print(f'\033[1;30;43m{"Contagem Regressiva":=^50}\033[m')

for x in range(10, 0, -1):
    print(f'É... {x}')
    time.sleep(1)
print(f'\033[1;33m{"Bum.. Feliz Ano Novo!":=^60}\033[m')