from math import pi
print('{:.^40}'.format('EX06 - Volume'))
altura = float(input('Entre com a altura: '))
raio = float(input('Entre com o valor do raio: '))
volume = pi * (raio * raio) * altura
print('Dada a altura {} o raio de {}, o volume do cilindro é:{:.2f}'.format(altura, raio, volume))
