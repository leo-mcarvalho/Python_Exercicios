print('{:.^40}'.format('EX05 - Verifica Ordem Crescente'))
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
    print('Os números foram digitados em ordem crescente')
else:
    print('Os números não foram digitados em ordem crescente')
