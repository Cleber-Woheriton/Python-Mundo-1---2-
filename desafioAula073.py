#(Desafio 73) Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
#  do Campeonato Brasileiro de Futebol, na Ordem de Colocação. Depois mostre;
# A) Os 5 primeiros colocados. B) Os últimos 4 colocados.
# C) Uma lista com os times em ordem alfabética. D) Em que posição está a chapecoense.

print(f'\033[1;30;43m{" Tabela do Campeonato Brasileiro ":=^70}\033[m')
pos = 17
cont = ind = 0
time = ''

tabela = ('Flamengo', 'Athletico', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Bragantino',
          'Fluminense', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Santos',
          'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Fortaleza', 'Sport',
          'São Paulo', 'América-MG')
print('Os cinco primeiros colocados são:')
print(f'{tabela[0: 5]}')
'''for c in range(0, 5):
    print(f'{c+1}º {tabela[c]}')'''
print(f'\033[1;30;43m{" Os últimos quatro colocados: ":=^70}\033[m')
print(tabela[-4:])
'''for c in range(4, 0, -1):
    print(f'{pos}º {tabela[-c]}')
    pos += 1'''
print(f'\033[1;30;43m{" A lista na ordem alfabética: ":=^70}\033[m')
print(sorted(tabela))
time = str(input('Deseja saber a posição de qual time?: ')).strip().title()
print(f'\033[1;30;43m{f" Lugar do {time}: ":=^70}\033[m')
if time in tabela:
    print(f'O {time} está na {tabela.index(time)+ 1}ª posição!')
else:
    print('O time não se classificou!')
