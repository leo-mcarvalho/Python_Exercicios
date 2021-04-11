print('{:.^40}'.format('EX09 - Venda com lucro'))
valor = float(input('Digite o valor do produto: '))
if valor <= 20:
    venda = valor + valor * 0.45
    print('O valor de venda do produto é de {:.2f}'.format(venda))
else:
    venda = valor + valor * 0.3
    print('O valor de venda do produto é de {:.2f}'.format(venda))
