#(Desafio 72) Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso de zero até vinte. Seu programa devera receber um valor int e
# retornar esse valor em extenso ex: 2 \ Dois.

print(f'\033[1;30;43m{" número por extenso de 0 - 20 ":=^70}\033[m')
numEx = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
         'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete',
         'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um valor entre (0-20): '))
while num > 20 or num < 0:
    num = int(input('Digite somente valores entre (0-20): '))
print(f'Você digitou o número \033[35m{numEx[num]}\033[m')
