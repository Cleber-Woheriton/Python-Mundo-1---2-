#(Desafio 65) Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o
# maior e o menor valor lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.

print(f'\033[1;30;43m{" Média dos Valores e Qual o Maior e o Menor  ":=^60}\033[m')

res = 'sim'
menor = maior = val = int
cont = media = 0

while res == 'sim':
    cont += 1
    val = int(input('Digite um valor inteiro: '))
    if val < 0:
        print('Valores negativos não são autorizados!')
        exit()
    if cont == 1:
        menor = val
        maior = val
    media += val
    if val < menor:
        menor = val
    elif val > maior:
        maior = val
    print('Deseja continuar? Sim ou Não?')
    res = str(input('Resposta: ')).strip().lower()
media = (media / cont)
print(f'\033[35m{"":~^70}\033[m')
print(f'Média dos valores digitados = \033[34m{media:.2f}'
      f'\033[m\nMaior valor digitado = \033[31m{maior}'
      f'\033[m\nMenor valor digitato = \033[32m{menor}\033[m')
print(f'\033[35m{"":~^70}\033[m')
