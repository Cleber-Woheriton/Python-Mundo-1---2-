#(Desafio 35) Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se elas podem ou não formar um triângulo.
print('=-'*15, '\033[1;30;43mÁrea do triângulo\033[m', '=-'*15)# Cód para cores
# \033[style(0,1,4,7) text(30 a 37) back(40 a 47) \033[m
#  *style da letra  *text cor do texto *back se trata da cor de fundo!
# pode usar três valores, dois valores ou um valor!
r1 = float(input('Valor do primeiro segmento: '))
r2 = float(input('Valor do segundo segmento: '))
r3 = float(input('Valor do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:# Fórmula para o triângulo!
    print('\033[1;30;47m Podem formar um triângulo!\033[m')
else:
    print('\033[1;30;47m Não podem formar um triângulo!\033[m')