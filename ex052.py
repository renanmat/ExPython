n = int(input('Digite um numero: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m', c, '\033[m', end='')
        cont += 1
    else:
        print('\033[31m', c, '\033[m', end='')
if cont == 2:
    print('\nO numero {1} é divisivel por {0} numeros, ele é PRIMO!'.format(cont, n))
else:
    print('\nO numero {} é divisivel por {} numeros, ele NAO é PRIMO!'.format(n, cont))
