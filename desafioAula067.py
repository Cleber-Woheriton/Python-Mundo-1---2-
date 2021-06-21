#(Desafio 67) Faça um programa que mostre a tabuada de vários números, um de cada
# vez, para cada vaalor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.

print(f'\033[1;30;43m{" Escolha a Tabuada ":~^70}\033[m')
fator = 0
result = int
fator2 = 1
while True:
    fator = int(input('Deseja ver a tabuada de qual valor: '))
    print(f'{"":~^70}')
    if fator < 0:
        break
    for fator2 in range(1, 11):
        result = fator * fator2
        print(f'{fator} x {fator2:2} = {result}')
    print(f'{"":~^70}')
print('Obrigado por usar nosso sistema!')
