print('{:.^40}'.format('EX06 - Impar ou Par'))
numero1 = int(input('Digite um número inteiro: '))
verifica = numero1 % 2
if verifica==0:
    print('O número {} é par'.format(numero1))
else:
    print('O número {} é ímpar'.format(numero1))
