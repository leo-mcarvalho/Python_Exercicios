print('{:.^40}'.format('EX009'))
n = int(input('Digite um número inteiro para ver sua tabuada '))
i = 1
print('-' * 13)
while i <= 10:
    print('{:02} x {:02} = {:02}'.format(n, i, n * i))
    i = i + 1
print('-' * 13)
