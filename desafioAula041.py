import time
from datetime import date
#(Desafio 41) A confederação nacional de natação, precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com
# a idade. "Até 9 - Mirim\ 14 - Infantil\ 19 - Júnior\ 25 - Sênior\ Acima - Master"
print('-='*10, '\033[30;43mCategoria Natação\033[m', '=-'*10)

ano = int(input('Ano de nascimento quatro dígitos: '))
print('\033[34mProcessando...\033[m')
atual = date.today().year
time.sleep(3)
ano = atual - ano
print(f'Idade atual: {ano} anos.')
if ano <= 9:
    print('Categoria Mirim!')
elif ano <= 14:
    print('Categoria Infantil!')
elif ano <= 19:
    print('Categoria Júnior!')
elif ano <= 25:
    print('Categoria Sênior!')
else:
    print('Categoria Master!')
