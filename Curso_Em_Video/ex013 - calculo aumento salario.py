print('{:.^40}'.format('EX013'))
salario = int(input('Informe seu salário atual: '))
aumento = int(input('Informe a porcentagem de aumento recebido: '))
valorTotal = salario + (salario * aumento / 100)
print('O seu salário era de R${}, e com o aumento de {}% ficou R${}'.format(salario, aumento, valorTotal))