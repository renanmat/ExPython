soma = 0
for cont in range(0, 6):
    num = int(input('Ditite um numero: '))
    if num % 2 == 0:
        soma += num
print('A soma dos numeros pares é igual a {}'.format(soma))
