print('{:.^40}'.format('EX04 - Abastecimento'))
combustivel_litro = float(input('Digite o preço do litro do combustível: '))
valor = float(input('Digite o valor que você deseja abastecer: '))
resultado = valor/combustivel_litro
print('Com o valor de R${}. Você consegue absastecer {:.2f}L'.format(valor, resultado))
