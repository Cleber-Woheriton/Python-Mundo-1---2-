fator1 = int(input('Tabuada do: '))

#def Tabuada(n1):
for x in range(10):
    fator2 = x +1
    produto = fator1 * fator2
    print(f'\033[7;33m {fator1}x{fator2:2} = {produto:2} \033[m')
else:
    print('Fim da Tabuada!')