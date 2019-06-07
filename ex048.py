soma = 0
n = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        n += 1
        soma += cont
print('A soma entre os numeros é \033[1;34m{}\033[m contendo \033[1;33m{}\033[m numeros.'.format(soma, n))
