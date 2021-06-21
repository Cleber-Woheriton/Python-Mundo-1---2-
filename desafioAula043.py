import time
#(Desafio 43) Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#"Abaixo de 18.5: Abaixo do Peso\ Entre 18.5 e 25: Peso ideal\ De 25 a 30: Sobrepeso\
# De 30 a 40: Obesidade\ Acima de 40: Obesidade Mórbida".
print('{:=^60}'.format(' \033[30;43mSistema de IMC\033[m '))
peso = float(input('Informe o peso Kg: '))
alt = float(input('Informe a altura m: '))
imc = peso / (alt ** 2)

print('\033[34mVerificando status...\033[m')
time.sleep(2)

if imc < 18.5:
    print('\033[33mAbaixo do Peso!')
elif 18.5 <= imc < 25:
    print('\033[32mPeso Ideal!')
elif 25 <= imc < 30:
    print('\033[33mSobrepeso!')
elif 30 <= imc <= 40:
    print('\033[33mObesidade!')
else:
    print('\033[31mObesidade Mórbida!')