lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    op = ' '
    while op not in 'nNsS':
        op = str(input('Quer continuar? [S/N]'))[0].lower().strip()
    if op == 'n':
        break
print('-='*30)

print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'Em ordem decrescente: {lista}')
if 5 in lista:
    print('Tem o valor 5 nesta lista')
else:
    print('Nao tem o valor 5 na lista')
