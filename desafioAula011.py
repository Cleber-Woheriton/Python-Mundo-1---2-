larg = float(input('Informe a largura: '))
alt = float(input('Informe a altura: '))


def calculaArea(larg, alt):
    mtq = alt * larg
    if mtq >= 2:
        litro = mtq
        print('Uma área de {:.0f} m² será necessário {:.1f} litro(s) de tinta!'.format(mtq, litro / 2))
    else:
        print('A baixo do padrão!')
    return larg, alt


format(calculaArea(larg, alt))
