from math import hypot

print('{:.^40}'.format('EX017'))
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
'''print('Considerando o cateto oposto {} e o cateto adjacente {}, o comprimento da hipotenusa é {}'.format(co, ca, math.sqrt(
    (co ** 2 + ca ** 2))))'''
print('Considerando o cateto oposto {} e o cateto adjacente {}, o comprimento da hipotenusa é {:.2f}'.format(
    hypot(co, ca)))
