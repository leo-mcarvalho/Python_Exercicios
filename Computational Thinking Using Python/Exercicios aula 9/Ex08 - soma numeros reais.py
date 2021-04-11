print('{:.^40}'.format('EX08 - Soma numeros reais'))
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
verifica = numero1 + numero2
if verifica > 10:
    print('A soma dos números digitados é maior que 10')
else:
    print('A soma dos números digitados é igual ou menor que 10')
