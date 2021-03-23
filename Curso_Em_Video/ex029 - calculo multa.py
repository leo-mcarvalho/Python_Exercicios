print('{:.^40}'.format('EX029'))
print('Radar da Via Expressa')
v = int(input('Digite a velocidade em que você passou pelo radar: '))
if v > 80:
    m = 7 * (v - 80)
    print('Congratulaixons mai friend, você ultrapassou o limite de velocidade! Você será multado em R${}'.format(m))
else:
    print('Infelizmente(para nós), você estava dirigindo dentro do limite de velocidade!')
