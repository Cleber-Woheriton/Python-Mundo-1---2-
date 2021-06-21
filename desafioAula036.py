# (Desafio 36) Escreva um programa para aprovar o empréstimo bancário para
# compra de uma casa. O programa vai perguntar o valor da casa, o saláro do comprador
# e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exeder 30% do salário ou então o empréstimo será negado!
print('=-' * 15, '\033[30;43mCalcula Empréstimo\033[m', '=-' * 15)
valorImov = float(input('Informe o valor do imóvel: '))
sal = float(input('Informe o seu salário: '))
anoPag = int(input('Por quantos anos irá pagar?: '))
meses = anoPag * 12
prestação = valorImov / meses
salario30 = sal * 30 / 100
if prestação <= salario30:
    print('\033[32mEmpréstimo Aprovado!\033[m')
    print(f'A parcela ficará em {meses} vezes de {prestação:.3f}')
else:
    print(f'\033[31mEmpréstimo Negado!\n O valor a ser pago seria de R$: {prestação:.3f}\033[m')
print('Tenha um bom dia!')