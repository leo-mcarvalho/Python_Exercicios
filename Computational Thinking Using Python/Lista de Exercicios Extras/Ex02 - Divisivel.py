print('{:.^40}'.format('EX02 - Divisivel'))
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

if numero1 % numero2 == 0:
    print('O número {} é divisível por {}'.format(numero1, numero2))
else:
    print('O número {} NÃO é divisível por {}'.format(numero1, numero2))
