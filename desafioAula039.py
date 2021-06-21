#(Desafio 39) Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com sua idade: "Se ele ainda vai se alistar ao serviço
# militar", "Se é hora de se alistar", "Se já passou do tempo de alistamento"
#  O programa também deverá mostrar o tempo que falta ou passou do prazo.
from datetime import date # importando para obter uma funçao do ano atual

print('-='*15, '\033[30;43mAlistamento\033[m', '=-'*15)
anoAtual = date.today().year # anoAtual recebendo ano atual.
ano = int(input('Informe o ano de nascimento: '))
idade = anoAtual - ano

if idade <= 18:
    print(f'Você tem {idade} anos de idade.\nAinda tem {18-idade} ano(s) para se alistar!')
elif 18 < idade <= 24:
    print(f'Idade atual: {idade}\nVocê precisa se alistar, tem até {idade - 18} ano(s) para se alistar!')
else:
    print(f'Idade atual: {idade}\nJá passou do tempo de se alistar, terá que pagar multa de {idade - 18} ano(s)')