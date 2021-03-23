print('{:.^40}'.format('EX011'))
l = float(input('Digite quantos metros sua parede tem de largura: '))
a = float(input('Digite quantos metro sua parede tem de altura: '))
m2 = l * a
print('Sua parede tem {:.1f}m² e seria necessário {:.1f} litros de tinta para pinta-la'.format(m2, m2 / 2))
