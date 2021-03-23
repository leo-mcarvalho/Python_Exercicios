print('{:.^40}'.format('EX022'))
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome
print(nome.upper())
print(nome.lower())
nome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nome[0])))
nome = ''.join(nome)
print('Seu nome completo sem espaços tem {}'.format(len(nome)))
