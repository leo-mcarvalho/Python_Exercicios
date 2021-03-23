print('{:.^40}'.format('EX027'))
n = input('Digite seu nome completo')
x = n.strip()
e = n.count(' ')
x = n.split()
#Ou da pra contar o numero de elementos de x com o len(x) e fazer -1 pra ficar igual a contagem do array que começa em 0
print('{}, seu primeiro nome é {} e o seu último nome é {}'.format(n, x[0], x[e]))
