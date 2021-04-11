print('{:.^40}'.format('EX01 - Prefeitura'))
while True:
    salario_bruto = float(input('Insira o valor do seu salário bruto: '))
    valor_prestacao = float(input('Qual o valor da prestação? '))
    if (salario_bruto > 0 and valor_prestacao > 0):
        break
    print('O valor do salário bruto e do valor da parcela tem que ser maiores que 0')
    print('-' * 40)

valor_max_prestacao = salario_bruto * 0.3
print('-' * 40)
print('Valor limite da prestação: {}'.format(valor_max_prestacao))

if (valor_prestacao > valor_max_prestacao):
    print('O seu empréstimo não pode ser concedido pois a parcela ultrapassa 30% do seu sálario bruto')
else:
    print('O seu empréstimo foi aprovado com sucesso!')
