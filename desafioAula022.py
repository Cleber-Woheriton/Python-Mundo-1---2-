# Crie um programa que leia o nome completo de uma pessoa e mostre.
# *O nome com todas as letras maiúsculas, *Nome com todas as letras minúsculas.
# *Quantas letras ao todo sem considerar espaços.
# *Quantas letras tem o primeiro nome.

# 1) Recebendo o nome
frase = str(input('Digite seu nome completo: '))

# 2) Deixando todas as letras maiúsculas.
frase = frase.upper()
print('Letras maiúsculas: ', frase)

# 3) Deixando as letras minúsculas.
frase = frase.lower()
print('Letras minúsculas: ', frase)

# 4) Letras ao todo sem considerar os espaços
frase1 = frase.strip()# A função está tirando espaços da direita e esquerda
frase1 = frase.split()# Está criando posições para cada frase e alocando na lista
frase1 = ''.join(frase1)
print('Quantia de letras no nome é de: ', len(frase1), ' Caracteres!')

# 5) Quantas letras tem o primeiro nome.
frase = frase.split()# Criando lista e armazenando as frases em cada posição.
p_nome = frase[0]# A variável p_nome esta recebendo o pimeiro nome dessa lista.
p_nome = p_nome.title()# Está transformando a primeira letra maiúscula.
print(f'O primeiro nome {p_nome} tem: ', len(frase[0]), ' letras!')
