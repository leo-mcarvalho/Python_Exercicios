#: abre o comando, o termo a seguir é o que vc quer preencher os espaços, o ^ é para o texto ficar no meio,
# o 20 é o tanto de campos que ele vai reservar pra isso.
print('{:.^40}'.format('EX006'))
n = int(input('digite um número '))
# Nesse caso para ficar 2 casas após o ponto usa-se : pra iniciar, . que é o ponto de referencia e 2f
# que são duas casas após a virgula
print('O dobro de {} é {}, o triplo é {} e a raíz quadrada dele é {:.3}'.format(n, n * 2, n * 3, n ** (1 / 2)))
# end=' ' no final do format não pula a linha, juntando o print atual com o de baixo na mesma linha
