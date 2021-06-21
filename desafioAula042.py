import time
#(Desafio 42) Refaça o desafio 35, acrescentando o recurso de informar qual tipo de
#triãngulo será formado. "Equilátero- Todos os lados iguais\ Isósceles- Dois lados iguais\
# Escaleno- Todos os lados diferentes."
print('-='*10, '\033[30;43m Área do Triângulo\033[m', '=-'*10)

valor = [[], [], []]
for x in range(0, 3):
    valor[x] = float(input(f'Digite o {x+1}º valor do segmento: '))
print('\033[36mProcessando...\033[m')
time.sleep(3)
if valor[0] < valor[1] + valor[2] and valor[1] < valor[0] + valor[2] and valor[2] < valor[0] + valor[1]:
    if valor[0] == valor[1] and valor[1] == valor[2]:# v[0] == v[1] == v[2]
        print('Triângulo Equilátero = Todos lados iguais!')
    elif valor[0] == valor[1] or valor[1] == valor[2] or valor[2] == valor[0]:
        print('Triângulo Isósceles = Dois lados iguais!')
    else:
        print('Triângulo Escaleno = Todos os lados diferentes!')
else:
    print('Não pode formar um triângulo!')