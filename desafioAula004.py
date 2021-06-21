import emoji

print(emoji.emojize('Olá emoji :woman: :droplet: :earth_asia:'))

char = input('Digite algo: ')
print('\033[7;33m Possuí espaços: ', char.isspace(), '\033[m')
print('\033[7;33m Possuí número: ', char.isnumeric(), '\033[m')
print('\033[7;33m É alfanumérioco: ', char.isalnum(), '\033[m')
print('\033[7;33m É alfabético: ', char.isalpha(), '\033[m')
#else:
 #   print('Outros tipos de valores ', type(char))
