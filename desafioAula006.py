n1 = input('Insira um número: ')

if n1.isnumeric():
    n1 = int(n1)
    print('O dobro do valor ({}) é ({}), e o triplo é ({}),'
          ' a raiz quadrada é ({})'.format(n1, n1*2, n1*3, n1**2))
else:
    print('Valor não numérico!')