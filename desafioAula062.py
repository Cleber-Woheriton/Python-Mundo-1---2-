#(Desafio 62) Melhore o desafio 61, perguntando ao usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer mostrar 0 termo.
import time

print(f'\033[1;30;43m{" Razão da P.A (Usando while) V0.1 ":=^60}\033[m')
termo = int(input('Primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = termo + ((10 - 1) * razao)
cont = 1
contador = 0

while cont != 0:
    while termo <= decimo:
        contador += 1
        print('\033[34m', termo, end='→ ')
        termo += razao
    print('Fim!')
    cont = int(input('\033[m\nQuer ver mais quantos termos? '))
    decimo = termo + ((cont - 1) * razao)

print(f'\033[35m{" Obrigado por usar nosso sistema! ":=^60}\033[m'
      f'\nProgressão finalizada com {contador} termos mostrados.')
