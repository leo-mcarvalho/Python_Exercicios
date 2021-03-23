print('{:.^40}'.format('EX07 - Prestacao'))
boleto = float(input('Entre com o valor do boleto: '))
juros = float(input('Entre com o juros cobrado: '))
dias = int(input('Entre com o numero de dias de atraso: '))
resultado = boleto + (boleto * (juros/100)) * dias
print('Atrasando o pagamento em {} dias, o novo valor a ser pago será de: R${:.2f}'.format(dias, resultado))
