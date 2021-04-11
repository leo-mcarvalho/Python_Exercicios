print('{:.^40}'.format('EX02 - Maior Número'))
numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))
print(40 * '-')
if numero1>numero2:
    print('O maior número entre os dois digitados é {}'.format(numero1))
elif numero1 <numero2:
    print('O maior número entre os dois digitados é {}'.format(numero2))
else:
    print('Os dois números são iguais!')