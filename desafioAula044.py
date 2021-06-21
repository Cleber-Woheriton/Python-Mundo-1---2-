import time


# (Desafio 44) Elabore um programa que calcule o valor a ser pago por um produto, considerando
# preço normal e condição de pagamento: " À vista dinheiro \ cheque: 10% de desconto.|
# À vista no cartão: 5% de descont | Em até 2x no cartão valor normal | 3x ou mais no
# cartão : 20% de juros"
def parcelado(valor):
    parc = int(input('Deseja parcelar em quantas vezes: '))
    if parc <= 0 or parc > 12:
        print('Parcelamento Inválido!')
    elif 0 < parc <= 2:
        print(f'Valor a pagar: 2x {valor / 2}')
    else:
        juros = valor + (valor * 20 / 100)
        print(f'Valor a pagar: {parc}x de {juros / parc:.2f}\nTotal do valor com juros R$: {juros}')


def realisarCompra(valor, opc):
    avista = int(input('À vista?\n Digite:\n 1 - (sim)\n 0 - (não): '))
    if avista == 1:
        if opc == ['Cartão de Crédito']:
            descCin = valor - (valor * 5 / 100)
            print(f'Sua compra de R$:{valor}, ficará à vista no cartão R$: {descCin:.2f}')
        elif opc == ['Cheque']:
            descDez = valor - (valor * 10 / 100)
            print(f'Sua compra de R$:{valor}, ficará à vista no cheque R$: {descDez:.2f}')
        else:
            descDez = valor - (valor * 10 / 100)
            print(f'Sua compra de R$:{valor}, ficará à vista no dinheiro R$: {descDez:.2f}')
    else:
        parcelado(valor)


print('-=' * 10, '\033[30;43mCalcular formas de pagamento\033[m', '=-' * 10)

opc = [['Cartão de Crédito'], ['Cheque'], ['Dinheiro']]
valor = float(input('Valor do produto R$: '))
print('\033[34mProcessando...\033[m')
time.sleep(3)
print('Formas de pagamento.')
print(' (1) - Cartão de Crédito \n (2) - Cheque'
      '\n (3) - Dinheiro')
formDePag = int(input('Forma de pagamento: '))
if formDePag == 1 or formDePag == 2 or formDePag == 3:
    opc = opc[formDePag - 1]
    esc = str(input(f'Opção escolhida é a \033[34m{opc}\033[m.\n Confirma? "Sim" ou "Não": '))
    esc = esc.lower()
    if esc in 'sim':
        print('Com sucesso!')
        realisarCompra(valor, opc)
    else:
        print('Operação não autorizada!')
else:
    print('\033[31mRefaça o processo...\033[m')
