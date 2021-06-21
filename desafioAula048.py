#(Desafio 48) Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print(f'\033[1;30;43m{" Soma de impares de (1 - 500) múltipos de 3 ":=^70}\033[m')
num = 0
imp = 0
for x in range(1, 501, 2): # (1, 501, 2), ele está pulando de 2 em 2, ou seja 1, 3, 5...
    if x % 3 == 0: # Aqui só pega os múltipos de 3 e soma na váriavel num
        imp += 1 # Contando os valores ímpares multiplos de três.
        num += x # somando os valores de x
print(f'Total de números ímpares de (1-500) múltiplos de 3 foram: {imp}\nA soma dos ímpares: {num}')
