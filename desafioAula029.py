#(Desafio 29) Escreva um programa que leia a velovidade de um carro.
# se ultrapassar 80km. Mostre uma msg dizendo que ele foi multado.
# A multa irá custar R$ 7.00 por cada km acima do limite.
print('*-'*15, 'Programa de Velocidade', '*-'*15)
vel = int(input('Informe a velocidade: '))

# if verificando se a velocidade é maior que 80Km
if vel > 80:
    acm = vel - 80# acm recebendo os Km acima dos 80Km
    print(f'\033[31m{vel} Km. Você foi multado o valor a pagar R$\033[33m {7 * acm}')
else:
    print('\033[32mVelocidade permitida!')