#(Desafio 23)  Faça um programa que leia um número de 0 a 9999 e mostrer na tela
# cada um dos dígitos separados.
# Ex; Digite um número:1834 {unidade: 4, dezena:3 centena:8 milhar:1}
num = int(input('Digite um número de 0 a 9999: '))
# Definindo uma condição para obter os valores corretos.
if num < 0:# Ex: -1, -2... não executa o código
    print('Valor Incorreto!')
if num > 9999:# Ex: 10000 +, também não executa o código!
    print('Valor Exedente!')
else:
    unidade = num // 1 % 10 # Divisão inteira por 1 e resto de divisão por 10
    dezena = num // 10 % 10 # Divisão inteira por 10 e resto de divisão por 10
    centena = num // 100 % 10 # Divisão inteira por 100 e resto de divisão por 10
    milhar = num // 1000 % 10 # Divisão inteira por 1000 e resto de divisão por 10
print('Analisando o valor:')
print(f'Unidade = {unidade}')
print(f'Dezena = {dezena}')
print(f'Centena = {centena}')
print(f'Milhar = {milhar}')