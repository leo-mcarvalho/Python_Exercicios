pal = input('Digite algo ')
print('O tipo primitivo desse valor é {}'.format(type(pal)))
print('Só tem espaços?', pal.isspace())
print('É um número?', pal.isnumeric())
print('É alfabético?', pal.isalpha())
print('É alfanumérico?', pal.isalnum())
print('Está escrito em letras maiúsculas?', pal.isupper())
print('Está escrito em letras minúsculas?', pal.islower())
print('Está capitalizada?', pal.istitle())