print('{:.^40}'.format('Checkpoint01'))
nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
while True:
    setor_feminino = float(input('Digite o valor total vendido no setor feminino: '))
    setor_masculino = float(input('Digite o valor total vendido no setor masculino: '))
    setor_infantil = float(input('Digite o valor total vendido no setor infantil: '))
    setor_beleza = float(input('Digite o valor total vendido no setor de beleza: '))
    if setor_feminino > 0 and setor_masculino > 0 and setor_infantil > 0 and setor_beleza > 0:
        break
    print(
        'O valor total vendido pelos setores tem que ser maiores que zero. Preencha novamente com os valores corretos')
    print('-'*40)

comissao_feminino = setor_feminino * 2 / 100
comissao_masculino = setor_masculino * 2 / 100
comissao_infantil = setor_infantil * 4 / 100
comissao_beleza = setor_beleza * 6 / 100
comissao_total = comissao_feminino + comissao_masculino + comissao_infantil + comissao_beleza
salario_total = salario + comissao_feminino + comissao_masculino + comissao_infantil + comissao_beleza
print('-'*40)
print('Prezado(a) {},\n'
      'Seu salário fixo é de {} reais e sua comissão referente ao mês vigente foi calculado em {} reais.\n'
      'Total a receber: {} reais'.format(nome, salario, comissao_total, salario_total))
