print('{:.^40}'.format('EX014'))
c = float(input('Digite a temperatura que você quer converter em Celsius: '))
print('{:.1f}°C em fahrenheit corresponde a {:.1f}ºF, e em kelvins corresponde a {:.1f}ºK'.format(c, (c * 1.8) + 32, c + 273.15))
