print('{:.^40}'.format('EX025'))
n = input('Digite seu nome completo: ')
if n.lower().__contains__('silva'):
    #OU da pra fazer 'silva' in n.lower - que vai verificar se tem silva em n
    print('{}, seu nome contem Silva'.format(n))
else:
    print('{}, seu nome não contem Silva'.format(n))
