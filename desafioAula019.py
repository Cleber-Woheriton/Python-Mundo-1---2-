# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que leia os nomes e escreva o nome escolhido
from random import choice
# import random
nom1 = str(input('Digite o primeiro nome: '))
nom2 = str(input('Segundo nome: '))
nom3 = str(input('Terceiro nome: '))
nom4 = str(input('Quarto nome: '))
lista = [nom1, nom2, nom3, nom4]
sorteado = choice(lista) # método usado para sortear um objeto da lista
# sorteado = random.choice(lista) # usado no cód import random.
print('O sorteado foi {}, para apagar o quadro!'.format(sorteado))