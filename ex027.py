n = str(input('Digite seu nome completo: ')).strip().title()
print('Seu primeiro nome é {}'.format(n.split()[0]))
nome = n.split()
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
