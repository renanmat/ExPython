def area(largura, comprimento):
    are = largura * comprimento
    print(f'A are do terreno {largura} X {comprimento} é igual {are}m2.')


# Programa principal
c = float(input('Qual a largura do terreno? '))
l = float(input('Qual o comprimento? '))
area(c, l)
