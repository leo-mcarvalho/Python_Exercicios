from math import sqrt

print('{:.^40}'.format('EX10 - Soma e raiz quadrada'))
escolha = int(input('=' * 62+ '\n'
                              'Digite o número correspondente a operação que deseja realizar\n'
                              '1 - Soma de dois números\n'
                              '2 - Raiz quadrada de um número\n'+'='*62+'\n'))
if escolha == 1:
    print('Soma de dois números\n')
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    print('A soma entre {} e {} é igual a {}'.format(num1, num2, num1 + num2))
elif escolha == 2:
    print('Raíz quadrada de um número')
    num = int(input('Digite o número para realizar a operação: '))
    print('A raíz quadrada de {} é {:.2f}'.format(num, sqrt(num)))
else:
    print('Opção inválida!')
    exit()
