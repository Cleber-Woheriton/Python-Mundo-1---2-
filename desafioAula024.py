#(Desafio 24) Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com o nome "SANTO".
cidade = str(input('Informe o nome da sua cidade: ')).strip()
cidade = cidade.lower()# Cidade recebe todo nome em minúsculo
cidade = cidade.split()# Coloca a frase em cada lista separadamente.Ex:[[] []]
if 'santo' in cidade[0]:# Dessa forma fica melhor ao ultilizar o if
    print('Sua cidade começa com o nome "Santo"!')
else:
    print('Sua cidade não começa com o nome "Santo"!')