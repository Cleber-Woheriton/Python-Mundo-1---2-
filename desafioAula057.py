#(Desafio 57) Faça um programa que leia o sexo de uma pessoa, mas só aceite os
# valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um
# valor correto!

print(f'\033[1;30;43m{" Ler Sexo Com While ":=^60}\033[m')
genero = ''
sexo = str(input('Informe o sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informe somente [M ou F]: ')).upper()
if sexo in 'MF':
    if sexo in 'M':
        genero = 'Masculino'
    else:
        genero = 'Feminino'

print(f'Obrigado você escolheu o sexo {genero}!\nSexo registrado.')

