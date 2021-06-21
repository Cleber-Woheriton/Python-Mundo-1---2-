#(Desafio 15) Escreva um programa que leia a Kilometragem percorrida e a
# quantidade de dias que foi alugado. Calcule o valor a pagar, sabendo que
# o carro custa R$60 por dia e R$0.15 por Km rodado.
km = float(input('Informe o Km percorrido: '))
dias = int(input('Dias alugado: '))
alDia = 60
kmRod = 0.15
total = (km * 0.15) + (dias * 60)
print(f'Valor a ser pago é de R$: \033[7;33m{total:.2f}\033[m')