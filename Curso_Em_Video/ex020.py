import random

print('{:.^40}'.format('EX020'))
alunos: list[str] = []
# '_' é uma convenção do Python para indicar que a variável não é usada no loop (pois só me interessa executar algo 15 vezes).
for _ in range(4):
    while True:
        try:
            alunos.append((input('Digite o nome de um aluno por vez: ')))
            break  # interrompe o while e vai para a próxima iteração do for
        except ValueError:
            print('Não foi digitado um nome')
random.shuffle(alunos)
# print('O sorteio para apresentação ficou assim:\n',random.sample(alunos,4))
print('O sorteio para apresentação ficou assim:\n', alunos)
