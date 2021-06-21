# print('Podemos unir dois prints em um com', end=' ')
# print('(end= e aspas simples), dendro e final do 1º parêntese, dessa forma! ')
print('Desafio 005 Python 3')
n1 = input('Digite um número inteiro: ')
if n1.isnumeric():
    n1 = int(n1)
    print('O número que você digitou é ({}), e seu antecessor é ({}), e seu sucessor ({})'.format(n1, n1-1, n1+1))
else:
    print('O valor não é um número inteiro')