print('{:.^40}'.format('EX01 - Média Ponderada'))

trabalho_laboratorio = float(input('Digite a sua nota do trabalho de laboratório: '))
avalicao_semestral = float(input('Digite a sua nota da sua avaliação semestral: '))
exame_final = float(input('Digite a sua nota do seu exame final: '))
print(40 * '-')
media = (trabalho_laboratorio * 0.2) + (avalicao_semestral * 0.3) + (exame_final * 0.5)

if media <= 4.9:
    nota = 'E'
elif media > 4.9 and media <= 5.9:
    nota = 'D'
elif media > 5.9 and media <= 6.9:
    nota = 'C'
elif media > 6.9 and media <= 7.9:
    nota = 'B'
else:
    nota = 'A'

print('Sua média ponderada foi de {:.2f}, sendo assim sua nota final é {}'.format(media, nota))
