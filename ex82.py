valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    op = str(input('Quer continuar? [S/N]'))[0].lower().strip()
    if op in 'nN':
        break
for cont in valores:
    if cont % 2 == 0:
        par.append(cont)
    else:
        impar.append(cont)
print(f'Valores digitados: {valores}')
print(f'Valores pares: {par}')
print(f'Valores impares: {impar}')
