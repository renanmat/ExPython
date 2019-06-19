matriz = [[], [], []]
par = terc = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Valor da posiçao [{linha}:{coluna}]:')))
print('-='*30)
maiorl = matriz[1][0]
for l in range(len(matriz)):
    for c in range(len(matriz)):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if matriz[1][c] > maiorl:
            maiorl = matriz[1][c]
    terc += matriz[l][2]
    print()
print('-='*30)
print(f'A soma dos numeros pares sao: {par}')
print(f'A soma dos numeros da 3° coluna é: {terc}')
print(f'O maior valor da linha 2° é: {maiorl}')
