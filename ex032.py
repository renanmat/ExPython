n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))
if n1 > n2 and n2 > n3:
    print('maior: {} e menor: {}'.format(n1, n3))
if n3 > n2 and n2 > n1:
    print('maior: {} e menor: {}'.format(n3, n1))
else:
    print('maior {} e menor: {}'.format(n2))
