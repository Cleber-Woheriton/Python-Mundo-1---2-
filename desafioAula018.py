import math
ang = float(input('Valor do ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {}º tem o seno de {:.2f}'.format(ang,seno))
print('O ângulo de {}º tem o cosseno de {:.2f}'.format(ang,cosseno))
print('O ângulo de {}º tem o tangente de {:.2f}'.format(ang,tan))