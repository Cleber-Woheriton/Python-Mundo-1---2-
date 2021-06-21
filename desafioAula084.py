#(Desafio 84) Faça um programa que leia o nome e peso de várias pessoas,
# quarde em uma lista. No final mostre: A)Total cadastrado B) Uma listagem com
# as pessoas mais pesadas C) Uma listagem com as pessoaas mais leves.

print(f'\033[1;43;30m{" Cadastro de Pessoas e Pesos ":=^60}\033[m')
pessoaLeve = []
pessoaPesada = []
dado = []
cont = 0
continuar = ''

while True:
    dado.append(str(input('Digite o nome: ')).strip().title())
    dado.append(float((input('Informe o peso: '))))
    if cont == 0:
        pessoaLeve.append(dado[:])
        pessoaPesada.append(dado[:])
    else:
        if dado[1] >= pessoaPesada[-1][1]:
            if dado[1] > pessoaPesada[-1][1]:
                pessoaPesada.clear()
                pessoaPesada.append(dado[:])
            else:
                pessoaPesada.append(dado[:])
        if dado[1] <= pessoaLeve[-1][1]:
            if dado[1] < pessoaLeve[-1][1]:
                pessoaLeve.clear()
                pessoaLeve.append(dado[:])
            else:
                pessoaLeve.append(dado[:])
    dado.clear()
    cont += 1
    continuar = str(input('Deseja continuar? [s/n]')).strip().lower()[0]
    if 'n' in continuar:
        print('Fim do cadastro.')
        break
print(f'Foram cadastradas um total de {cont} pessoas.')
print(f'O maior peso foi de {pessoaPesada[0][1]:.1f}Kg. Peso de', end=' |')
for c in range(len(pessoaPesada)):
    print(pessoaPesada[c][0], end='|')
print(f'\nO menor peso foi de {pessoaLeve[0][1]:.1f}Kg. Peso de', end=' |')
for c in range(len(pessoaLeve)):
    print(pessoaLeve[c][0], end='|')
