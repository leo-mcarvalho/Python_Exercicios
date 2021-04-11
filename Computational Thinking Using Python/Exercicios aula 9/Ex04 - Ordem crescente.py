print('{:.^40}'.format('EX04 - Ordem Crescente'))
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
if numero1 == numero2 and numero2 == numero3:
    print('Os três números digitados são iguais')
else:
    numeros = [numero1, numero2, numero3]
    numeros.sort(reverse=True)
    print('A ordem crescente dos números digitados é {}'.format(numeros))
