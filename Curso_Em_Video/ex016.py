from math import trunc

print('{:.^40}'.format('EX016'))
n = float(input('Digite um número real: '))
print('O número {} tem como parte inteira {}'.format(n, trunc(n)))
