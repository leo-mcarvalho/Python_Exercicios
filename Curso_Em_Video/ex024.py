print('{:.^40}'.format('EX024'))
c = input('Digite o nome de uma cidade para saber se ela começa com "Santo": ')
d = c.strip()
d = c.split()
if d[0].lower() == 'santo':
    print('A Cidade, {}, começa com "Santo"'.format(c))
else:
    print('A Cidade, {}, não começa com "Santo"'.format(c))
