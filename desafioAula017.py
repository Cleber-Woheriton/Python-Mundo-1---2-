import math
#Não resolvi assisti ao vídeo(Exercício Python #017​ - Catetos e Hipotenusa)
#Importei o Math pois irei usar a funçaõ:  hypot(x,y)
catO = float(input('Digite o valor do cateto oposto: '))
catA = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(catO, catA)
print('A hipotenusa mede: {:.2f}'.format(hi))