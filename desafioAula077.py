# (Desafio 77) Crie um programa que tenha uma tupla com várias palavras
# (sem acentos). Deve ser mostrado para cada palavra, quais são as suaas vogais.
print(f'\033[1;30;43m{" Vogais das palavras ":=^70}\033[m')
print('\033[33mEscreva palavras sem acentuação!\033[m')

palav = (str(input('Escreva uma palavra qualquer: ')).strip().lower(),
         str(input('Escreva outra palavra qualquer: ')).strip().lower(),
         str(input('Última uma palavra : ')).strip().lower())
val = len(palav)
for c in range(val):
    a = e = i = o = u = 0
    carreto = ''
    if 'a' in palav[c] or 'e' in palav[c] or 'i' in palav[c] \
            or 'o' in palav[c] or 'u' in palav[c]:
        palavra = palav[c]
        if 'a' in palavra:
            a = palavra.count('a')
            carreto += f'{a}(A)'
        if 'e' in palavra:
            e = palavra.count('e')
            carreto += f'{e}(E)'
        if 'i' in palavra:
            i = palavra.count('i')
            carreto += f'{i}(I)'
        if 'o' in palavra:
            o = palavra.count('o')
            carreto += f'{o}(O)'
        if 'u' in palavra:
            u = palavra.count('u')
            carreto += f'{u}(U)'
        print(f'A palavra {palavra} possuí {carreto}')
    t = int(a + e + i + o + u)
    if t <= 0:
        print('As palavras não possuem vogais')
        exit()



'''for l in palav: #Solução do curso
    print(f'\nA palavra {l} possuí as vogais: ', end='')
    for letra in l:
        if letra in 'aeiou':
            print(letra, end=' ')'''
