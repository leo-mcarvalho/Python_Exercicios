import random
from time import sleep

print('{:.^40}'.format('EX028'))
print('{:-^40}\n'.format('Jogo da Advinhação!'), 40 * '=')
print('Deixe-me pensar em um número...')
sleep(3)
n = int(input('Computador: Tente Advinhar que número estou pensando entre 0 e 100: '))
s = random.randint(0, 100)
if n == s:
    print('ulala Parabéns você acertou! O número que eu estava pensando era {}'.format(s))
else:
    print('Poxa vida, você errou! O número que eu estava pensando era {}'.format(s))
