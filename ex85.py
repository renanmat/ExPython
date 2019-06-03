lista = [[], []]
for cont in range(0, 7):
    num = int(input(f'Digite o {cont+1}° numero: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Numeros pares: {sorted(lista[0])}')
print(f'Numeros impares: {sorted(lista[1])}')
