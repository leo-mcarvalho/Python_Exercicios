print('{:.^40}'.format('EX031'))
d = float(input('Digite a distancia que você quer percorrer em km: '))
if d > 200:
    x = d * 0.45
    print('O valor da viagem é R${:2}'.format(x))
else:
    x = d * 0.5
    print('O valor da sua viagem é R${:2}'.format(x))
