print('{:.^40}'.format('EX015'))
km = float(input('Quantos km você percorreu com o carro? '))
d = int(input('Quantos dias você utilizou o carro? '))
print('Você utilizou o carro por {} dias, andou com ele {}km e o total a ser pago é R${}'.format(d, km,
                                                                                                 d * 60 + km * 0.15))
