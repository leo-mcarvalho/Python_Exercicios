print('{:.^40}'.format('EX07 - Notas aluno'))
aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))
nota3 = float(input('Insira a terceira nota do aluno: '))
faltas = int(input('Insira a quantidade de faltas do aluno: '))
media = (nota1 + nota2 + nota3) / 3
if faltas >= 20:
    print('O aluno {}, teve {} faltas e está Reprovado por falta!'.format(aluno, faltas))
    exit()
elif media < 7:
    print('O aluno {}, teve média final {:.2f}, portanto está Reprovado por média!'.format(aluno, media))
    exit()
print('O aluno {}, teve média final {:.2f}, está Aprovado!'.format(aluno, media))
