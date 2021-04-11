print('{:.^40}'.format('EX06 - Tipos de triangulos'))
segmento1 = float(input('Digite o primeiro segmento de reta: '))
segmento2 = float(input('Digite o segundo segmento de reta: '))
segmento3 = float(input('Digite o terceiro segmento de reta: '))

lados = [segmento1, segmento2, segmento3]
lados.sort(reverse=-1)
if lados[1] + lados[2] <= lados[0]:
    print('Dados inválidos para construção do triangulo')
else:
    if lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
        print('Baseado nas informções digitadas esse é um triângulo escaleno')
    elif lados[0] == lados[1] and lados[0] == lados[2] and lados[1] == lados[2]:
        print('Baseado nas informções digitadas esse é um triângulo equilátero')
    else:
        print('Baseado nas informções digitadas esse é um triângulo isóceles')