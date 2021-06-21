nota1 = float(input('Entre com a 1º nota: '))
nota2 = float(input('Entre com a 2º nota: '))


def calculaMedia(nota1, nota2):
    med = float(nota1 + nota2) / 2
    print('Média: ',med)
    return med


format(calculaMedia(nota1, nota2))
