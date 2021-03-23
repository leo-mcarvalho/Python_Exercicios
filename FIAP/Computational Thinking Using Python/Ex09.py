print('{:.^40}'.format('EX09 - Apuração'))
candidato_a = int(input('Digite quantos votos o candidato A recebeu: '))
candidato_b = int(input('Digite quantos votos o candidato B recebeu: '))
candidato_c = int(input('Digite quantos votos o candidato C recebeu: '))
voto_branco = int(input('Digite quantos votos foram brancos: '))
voto_nulo = int(input('Digite quantos votos foram nulos: '))
print('-' * 40)
total_votos = candidato_a + candidato_b + candidato_c + voto_branco + voto_nulo

def percentual_votos(x):
    x = (x * 100) / total_votos
    return x

porcentagem_a = percentual_votos(candidato_a)
porcentagem_b = percentual_votos(candidato_b)
porcentagem_c = percentual_votos(candidato_c)
porcentagem_branco = percentual_votos(voto_branco)
porcentagem_nulo = percentual_votos(voto_nulo)

'''
porcentagem_a = (candidato_a * 100) / total_votos
porcentagem_b = (candidato_b * 100) / total_votos
porcentagem_c = (candidato_c * 100) / total_votos
porcentagem_branco = (voto_branco * 100) / total_votos
porcentagem_nulo = (voto_nulo * 100) / total_votos
'''

print('O total de eleitores foi de {}\n'
      'O candidato A recebeu {:.2f}% dos votos\n'
      'O candidato B recebeu {:.2f}% dos votos\n'
      'O candidato C recebeu {:.2f}% dos votos\n'
      'Houveram {:.2f}% de votos brancos\n'
      'Houveram {:.2f}% de votos nulos'.format(total_votos, porcentagem_a, porcentagem_b, porcentagem_c,
                                               porcentagem_branco, porcentagem_nulo))
