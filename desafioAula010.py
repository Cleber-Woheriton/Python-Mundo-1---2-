real = float(input('Valor em real R$: '))
realDolar = 0.17
dolar = real * realDolar

print(f'R$:\033[32m {real} \033[m reais compra-se US$:\033[31m {dolar:.1f} \033[m, em dólar(es)')