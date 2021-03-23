print('{:.^40}'.format('EX032'))
a=int(input('Digite um ano para saber se ele é bissexto: '))
if a%4==0 and a%100 != 0:
   print('{} é um ano bissexto!'.format(a))
else:
    print('{} não é um ano bissexto'.format(a))