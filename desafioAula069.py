#(Desafio 69) Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final mostre{A)Quantas pessoas tem mais de 18 anos. B)Quantos homens foram cadastrados
# C)Quantas mulheres tem menos de 20 anos.}

print(f'\033[1;30;43m{" Cadastrar Pessoa ":=^70}\033[m')

idade = contI = contH = contM = n = 0
sexo = res = ''
while True:
    n += 1
    print(f'{"":=^70}')
    print(f'{f" Cadastramento da {n}º Pessoa ":^70}')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().lower()[0]
    while sexo not in 'mf':
        sexo = str(input('Sexo[M/F]: ')).strip().lower()[0]
    if idade >= 18:
        contI += 1
    if sexo in 'm':
        contH += 1
    if sexo in 'f':
        if idade < 20:
            contM += 1
    res = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    while res not in 'sn':
        res = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if res in 'n':
        print('Fim do Cadastro.')
        print(f'{"":=^70}')
        print(f'Foram Cadastrados\n({contI}) Pessoa(s) +18'
              f'\n({contH}) Homen(s)\n({contM}) Mulher(es) com menos de 20 anos.')
        break

