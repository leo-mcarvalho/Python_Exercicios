print('{:.^40}'.format('EX03 - Ordem Decrescente'))
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

numeros=[numero1,numero2,numero3]
numeros.sort(reverse=False)
print('A ordem decrescente dos números digitados é {}'.format(numeros))