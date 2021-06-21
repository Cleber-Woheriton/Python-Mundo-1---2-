frase = str(input('Digite uma frase qualquer: '))
frase = frase.lower()
# len() é uma função que conta total de caracteres ou lista
print('A frase "{}", tem um total de {} caracteres!'.format(frase, len(frase)))
print(frase.count('a'))
