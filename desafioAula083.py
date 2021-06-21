#(Desafio 83) Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu app deverá analisar se a expressão está com os
#  parênteses abertos e fechados na ordem correta.
print(f'\033[1;30;43m{" Verifica Expressão ":=^70}\033[m')
parent1 = []
exp = str(input('Informe a expressão: '))
for c in exp:
    if exp[0] in ')':
        print('\033[31mExpressão inválida!\033[m')
        exit()
    if '(' in c:
        parent1.append('(')
    if ')' in c:
        if len(parent1) > 0:
            parent1.pop()
        else:
            parent1.append(')')
if len(parent1) == 0:
    print('\033[32mExpressão válida!\033[m')
else:
    print('\033[31mExpressão inválida!\033[m')