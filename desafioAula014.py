#(Desafio 14) Escreva um programa que leia uma temperatura digitada
# em ºC e converta em ºF.
temp = float(input('Informe a temperatura em ºC:'))
f = ((9 * temp)/5) + 32
print(f'A temperatura informada em ºC, agora em ºF: {f}')