print('{:.^40}'.format('EX03 - Instituição Bancária'))
num_conta = int(input('Informe o número da sua conta\n'))
# invertendo o numero na marra usando matematica
test1 = num_conta % 100
n1 = num_conta // 100  # primeiro numero
n2 = test1 // 10  # segundo numero
n3 = test1 % 10  # terceiro numero

inverte = n3 * 100 + n2 * 10 + n1  # faz conta para trazer o valor invertido
soma = num_conta + inverte

test2 = soma % 100
test3 = soma // 100
test4 = test2 // 10
test5 = test2 % 10




