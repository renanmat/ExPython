nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiusculo: {}'.format(nome.upper()))
print('Seu nome em minusculo: {}'.format(nome.lower()))
dividido = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))
print('Quantidade de letras ao todo: {}'.format(len(nome)- nome.count(' ')))

##print('Quantidade de letras no nome ao todo tem: {}'.format(len(''.join(dividido))))
