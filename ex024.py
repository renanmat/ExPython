c = str(input('Digite um nome de cidade: ')).strip() ## elimina os espaços
print('Seu primeiro nome começa com santo: {}'.format('santo' in c.lower().split()[0]))
