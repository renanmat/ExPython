ex = str(input('Digite a expressao: '))
lista = []
for num in ex:
    if num == '(':
        lista.append(num)
    elif num == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(num)
            break

if len(lista) == 0:
    print('Sua expressao esta \033[1;4;32mValida\033[m!')
else:
    print('Sua expresssao esta \033[1;4;31mInvalida\033[m!')
