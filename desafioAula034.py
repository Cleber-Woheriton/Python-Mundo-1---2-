#(Desafio 34) Escreva um programa que pergunte o salário de um
# funcionário e calcule o valor do seu aumento.
print('*-'*10, 'Calcula aumento do funcionário', '*-'*10)

sal = float(input('Informe seu salário: '))


if sal < 800:
    print('Não consta na folha de pagamentos!')

elif sal <= 1.250:
    auQuin = sal * 15 / 100
    print(f'Seu salário terá um aumento de 15% : {sal + auQuin}')

else:
    auDez = sal * 10 / 100
    print(f'Seu salário terá um aumento de 10% : {sal + auDez}')

