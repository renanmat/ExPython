a = input('Digite qualquer coisa ')
print('Seu tipo primitivo {}'.format(type(a)))
print('Tem so empaço?', a.isspace())
print('É numero?', a.isnumeric())
print('tem so letras? ', a.isalpha())
print('É alfanumerico? {}\nEsta em maiusculo? {}\nEsta em minusculo? {}'.format(a.isalnum(),a.isupper(),a.islower()))
print('Esta capsulado? ', a.istitle())

