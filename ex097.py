def escreva(texto):
    c = len(texto) + 4
    print('~'*c)
    print(f'{texto:^{c}}')
    print('~'*c)


# Programa principal
txt = str(input('Ecreva uma fraze: ')).strip()
escreva(txt)
