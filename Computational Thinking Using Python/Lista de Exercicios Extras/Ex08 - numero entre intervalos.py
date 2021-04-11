print('{:.^40}'.format('EX08 - Numero entre intervalos'))
numero = int(input('Digite um número: '))
if numero <= 30 and numero >= 0:
    print('O número {} está compreendido entre 0 e 30'.format(numero))
elif numero <= 79 and numero >= 40:
    print('O número {} está compreendido entre 40 e 79'.format(numero))
else:
    print('O número {} está fora dos limites estabelecidos'.format(numero))