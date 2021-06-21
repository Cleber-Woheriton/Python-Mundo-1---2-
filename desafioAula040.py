#(Desafio 40) Crie um programa que leia duas notas de um aluno e calcule sua
# média, mostrando uma msg no final, de acordo com a média atingida.
# "Média a baixo de 5.0 - Reprovado, entre 5.0 e 6.5 - Recupeeração, 7.0 ou
# superior - Aprovado".
print('-='*15, '\033[30:43mMédia Final\033[m', '=-'*15)
nota = [[], []]

nota[0] = float(input('Digite a primeira nota: '))
nota[1] = float(input('Digite a segunda nota: '))

média = (nota[0] + nota[1]) / 2

if média >= 7:
    print(f'\033[32mVocê está aprovado!\033[m\nSua média é: {média:.2f}')
elif 5 <= média <= 6.9:
    print(f'\033[33mVocê está em recuperação!\033[m\nSua média atual é: {média:.2f}')
else:
    print(f'\033[31mVocê está reprovado!\033[m\nSua média é: {média:.2f}')
print('\033[33m=-=-Bons estudos!=-=-\033[m')