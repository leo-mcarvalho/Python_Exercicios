print('{:.^40}'.format('EX03 - Cotacao'))
cotacao_dolar = float(input('Entre com a cotação do dolar: '))
reais = float(input('Entre com o valor em reais que deseja realizar a conversão: '))
conversao = reais / cotacao_dolar
print('Com o valor de R${}. Você consegue comprar ${:.2f}'.format(reais, conversao))
