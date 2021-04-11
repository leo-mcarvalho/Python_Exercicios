print('{:.^40}'.format('EX07 - Multiplo de 5 e 10'))
numero1 = int(input('Digite um número inteiro: '))
verifica = numero1 % 5
verifica2 = numero1 % 10
if verifica == 0 and verifica2 == 0:
    print('O número {} é múltiplo de 5 e 10 ao mesmo tempo'.format(numero1))
else:
    print('O número {} não é múltiplo de 5 e 10 ao mesmo tempo'.format(numero1))
