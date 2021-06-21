#Faça um programa que leia o nome de quatro alunos e imprima a ordem de apresentação.
#import random
from random import shuffle
nom1 = str(input('Digite o nome: '))
nom2 = str(input('Digite o nome: '))
nom3 = str(input('Digite o nome: '))
nom4 = str(input('Digite o nome: '))
lista = [nom1, nom2, nom3, nom4]
shuffle(lista) # shuffle é um método do random para embaralhar as posiçoes!
#random.shuffle(lista)
print('A ordem da apresentação será =>{}'.format(lista))