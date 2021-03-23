import random

print('{:.^40}'.format('EX019'))
alunos: list[str] = []
alunos.append((input('Digite o nome do primeiro aluno: ')))
alunos.append((input('Digite o nome do segundo aluno: ')))
alunos.append((input('Digite o nome do terceiro aluno: ')))
alunos.append((input('Digite o nome do quarto aluno: ')))
#x = random.randint(0, 3)
#print('O aluno sorteado para apagar o quadro foi....{}!'.format(alunos[x]))
x=random.choice(alunos)
print('O aluno sorteado para apagar o quadro foi....{}!'.format(x))
