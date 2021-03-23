print('{:.^40}'.format('EX034'))
s = float(input('Digite o seu salário: '))
if s > 1250:
    s = s + (s * 10 / 100)
    a = 10
else:
    s = s + (s * 15 / 100)
    a = 15
print('O seu salário com o aumento de {}% é de R${:2}'.format(a, s))
