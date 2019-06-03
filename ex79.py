numeros = []

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('foi adicionado...')
    else:
        print('numero duplicado, nao foi add...')
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar[s/n]? '))[0].lower()

    if op in 'nN':
        break

print(numeros)