op = 0
while op != 5:
    n1 = int(input('Digite o 1º numero: '))
    n2 = int(input('Digite o 2º numero: '))
    print("""    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa""")
    op = int(input('Escolha uma opção: '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, (n1+n2)))
    elif op == 2:
        print('{} X {} = {}'.format(n1, n2, (n1*n2)))
    elif op == 3:
        if n1 > n2:
            print('O maior numero é o {}'.format(n1))
        else:
            print('O maior numero é o {}'.format(n2))
print('FIM.')
