print('{:.^40}'.format('EX08 - Milionario'))
salario = float(input('Entre com o seu salário: '))
despesas_mensais = float(input('Entre com o valor das suas despesas: '))
sobra_anual = (salario - despesas_mensais) * 12
anos = 1000000 // sobra_anual
print('Atualmente você está poupando R${} por ano, se continuar assim faltam {:.0f} anos para você ficar milionario'.format(sobra_anual,anos))
