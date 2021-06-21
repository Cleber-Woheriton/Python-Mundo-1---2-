#(Desafio 30) Crie um programa que leia um número inteiro e mostre na tela
# se ele é "Par" ou "Impar".
print('*-'*15, '\033[30;43mVerifica número\033[m', '*-'*15)
num = int(input('Digite um número: '))

if num % 2 == 0:
    print('O número informado é par!')
else:
    print('O número informado é impar!')