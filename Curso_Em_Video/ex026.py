print('{:.^40}'.format('EX026'))
f = str(input('Digite uma frase qualquer: ')).strip()
x = f.lower()
a = x.count('a')
x = x.find('a')
b = x.rfind('a')
print(
    'Na frase "{}"\nAparece a letra "a" {} vezes, a primeira, aparece na posição {}, a última aparece na posição {}'.format(
        f, a, x+1, b+1))
