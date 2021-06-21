#(Desafio 26) Faça um programa que leia uma frase, e mostre quantas vezes
# aparece a letra "A", em que posição aparece na primeira vez e a última vez.
print('*'*30)
print('Quantas letras "a", possuí na frase:')
frase = str(input('Digite a frase: '))
frase = frase.lower()# Transformando em minúsculo e atribuindo a frase.
if 'a' in frase:# Comparando se a frase possuí a letra "a".
    print('A letra "a", aparece {} na frase!'.format(frase.count('a')))
    print('A primeira letra "a", aparece na posição: ', frase.find('a'))
    print('A última letra "a", aparece na posição: ', frase.rfind('a'))
else:# Caso não possua a letra "a"
    print('A frase não possuí a letra "a"!')