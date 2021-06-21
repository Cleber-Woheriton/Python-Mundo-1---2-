#(Desafio 53) Crie um programa que leia uma frase qualquer e diga se ela é um
# polindromo, desconsiderando os espaços.
import time

print(f'\033[1;30;43m{" Palindromo ":=^60}\033[m')
frase = ''
frase = str(input('Digite uma frase: '))
print('\033[33mLogo saberá se ela é palindromo ou não!\033[m')
time.sleep(2)
frase1 = frase.split()
frase1 = "".join(frase1)
frase1 = frase1.lower()
tam = len(frase1)
#inverso = ''
inverso = frase1[::-1]
if frase1 == inverso: # Solução do Curso
    print(f'\033[30;42mÉ um PAINDROMO!\033[m')
else:
    print('\033[30;41mNão é um PALINDROMO!\033[m')
'''for x in range(tam, 0, -1):# Minha solução
    inverso += frase1[x - 1]
    if frase1 == inverso:
        if x == 1:
            print(f'\033[30;42mÉ um PAINDROMO!\033[m')
    else:
        if x == 1
            print('\033[30;41mNão é um PALINDROMO!\033[m')'''
print(f'A frase {frase}, invertida é: {inverso}.\nFim!')

