#(Desafio 31) Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o valor da passagem, em R$ 0.50c por Km em
# até 200Km e R$ 0.45c em viagens mais longas


def viajar(distancia):
    if distancia <= 200:
        print(f'Sua viagem irá lhe custar R$: {distancia*0.50}')
    else:
        print(f'Sua viagem ira lhe custar R$: {distancia*0.45}')

print('*-'*15, 'Calcula Viagem', '*-'*15)
distancia = float(input('Infome a distância: '))

if distancia <= 0:
    print('Viagem não iniciada!')
else:
    viajar(distancia)