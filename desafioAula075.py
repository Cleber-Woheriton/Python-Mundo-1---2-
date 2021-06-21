# (Desafio 75) Desenvolva um programa que leia quatro valores pelo teclado e
# guarde-os em uma tupla. No final mostre A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.
print(f'\033[1;30;43m{" Inserir Números na Tupla ":=^70}\033[m')
n = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
     int(input('Digite mais número: ')), int(input('Digite o último número: ')))
fal = 0
print(f'Os números digitados foram {n}')
print(f'O número 9 apareceu {n.count(9)} vezes!')
if 3 in n:
    print(f'O primeiro 3 apareceu na {n.index(3)+1}ª posição!')
else:
    print('O número 3 não foi digitado!')
print('Os números pares: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
    else:# Fiz isso caso não tenha nenhum número par!
        fal += 1
    if fal == 4:
        print('\nNão foi informado nenhum número par!')
