numeros = []
maior = menor = 0
posmenor = posmaior = 0
for n in range(0, 5):
    numeros.append(input(f'digite o {n+1} valor: '))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print(f'O maior numero é {maior} na pos ', end=' ')
for pos, n in enumerate(numeros):
    if n == maior:
        print(pos, end='...')
print(f'\nO menor numero é {menor} na pos', end=' ')
for pos, n in enumerate(numeros):
    if n == menor:
        print(pos, end='...')