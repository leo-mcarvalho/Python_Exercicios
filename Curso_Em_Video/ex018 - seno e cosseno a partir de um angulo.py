from math import tan, cos, sin, radians

print('{:.^40}'.format('EX018'))
g = float(input('Digite um ângulo entre 0º e 360º: '))
r = radians(g)
print('O ângulo de {:.2f}º tem como seno {:.2f} e como cosseno {:.2f} e tangente {:.2f}'.format(g, sin(r), cos(r),
                                                                                                tan(r)))
