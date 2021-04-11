print('{:.^40}'.format('EX04 - Teste de Mesa'))

numero1 = int(input('Digite um número inteiro'))
numero2 = int(input('Digite outro número inteiro'))
print(numero1 % 2)
resultado = ((numero1 % 2) * 3) + (13 - 2 + numero2)
if resultado <= 0:
    print('Resultado menor ou igual a zero')
else:
    if resultado > 0 and (resultado <= 20):
        print('Resultado maior que zero e menor ou igual a 20')
    else:
        print('Resultado maior que 20')

# a - 20
# b - Resultado maior que zero e menor ou igual a 20
