print('{:.^40}'.format('EX03 - Instituição Bancária'))
num_conta = (input('Informe o número da sua conta\n'))
revertido = num_conta[::-1]
soma = int(num_conta) + int(revertido)
stringe = str(soma)
i = 0
calculo = 0
for i in range(len(stringe)):
    calculo = calculo + int((stringe[i] * (i + 1)))
    #print('valor i ', i)
    #print('valor ', stringe[i])
calculo = str(calculo)
digito = calculo[len(calculo) - 1]
print('O digito verificador da sua conta é {}'.format(digito))

