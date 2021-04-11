print('{:.^40}'.format('EX02 - Companhia Aerea'))
while True:
    destino = int(input('Digite o numero de acordo com a região que você quer viajar:\n'
                        '1 - para região Norte\n'
                        '2 - para região Nordeste\n'
                        '3 - para região Centro-Oeste\n'))

    escolha = {1: 'Norte', 2: 'Nordeste', 3: 'Centro-Oeste'}

    ida_volta = input('Gostaria de comprar ida e volta ou somente ida?\n').lower()

    if (destino <= 3 and destino >= 1 and ida_volta == 'ida' or ida_volta == 'ida e volta'):
        print('-' * 40)
        break
    print('Preencha os campos corretamente!')
    print('-' * 40)
regiao = list(escolha.values())[destino]
if (ida_volta == 'ida'):
    precos = [280, 380, 620]
else:
    precos = [400, 628, 1100]
preco = list(escolha.keys())[destino]
print('O destino escolhido foi {}, o valor total a ser pago pela passagem de {} é de R${}'
      .format(regiao, ida_volta, precos[preco - 1]))

