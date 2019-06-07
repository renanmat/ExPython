cr = {'am': '\033[1;33m', 'l': '\033[m', 'az': '\033[1;34m'}
frase = str(input('Digite uma frase: ')).strip().upper()
frasejunta = ''.join(frase.split())
frase2 = frasejunta[::-1]
####################################################
# outra maneira de inverter a frase utilizando o FOR:
"""frase2 = '' 
for c in range(len(frasejunta)-1, -1, -1):
    frase2 += frasejunta[c]"""
####################################################
print('O inverso de {2}{0}{3} é {4}{1}{5}.'.format(frase, frase2, cr['az'], cr['l'], cr['am'], cr['l']))
if frase2 == frasejunta:
    print('Essa frase é um Palíndromo!')
else:
    print('Essa frase NÃO é um Palíndromo!')
