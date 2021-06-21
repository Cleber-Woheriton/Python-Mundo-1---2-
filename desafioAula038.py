#(Desafio 38) Escreva um programa que leia 2 números inteiros e compare-os,
# mostrando na tela uma mensagem: "O primeiro valor é maior!",
# "O segundo valor é maior!" ou "Não existe valor maior os dois são iguais!"
print('-='*15, '\033[30;43mMaior Valor\033[m', '=-'*15)
num = [[], []]
num[0] = int(input('Digite o 1º valor: '))
num[1] = int(input('Digite o 2º valor: '))

if num[0] > num[1]:
    print('O primeiro valor é maior! ', num[0])
elif num[1] > num[0]:
    print('O segundo valor é maior! ', num[1])
else:
    print('Não tem número maior, os dois são iguais!')