print('{:.^40}'.format('EX033'))
print('Qual número é maior?')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

n = [n1, n2, n3]
n.sort(reverse=True)
print('O maior número entre os três é o {} e o menor é o {}'.format(n[0], n[2]))
