#(Desafio 27) Faça um programaa que leia o nome completo da pessoa, monstrando em
# seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: '))
nome = nome.split()
val = int(len(nome)) - 1
print('Bem vindo, {} {}'.format(nome[0], nome[val]))
