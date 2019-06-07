cor = {'fim': '\033[m', 'azul': '\033[1;4;34m', 'vermelho': '\033[1;4;31m', 'verde': '\033[1;4;32m'}
from time import sleep
soma = cont = maior = 0
op = 's'
n = menor = int(input('Digite um numero: '))
while op in 'sS':
    cont += 1
    if cont > 1:
      n = int(input('Digite um numero: '))
    soma += n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    op = str(input('Quer digitar outro numero? ')).strip()[0]
print('Analizando os dados...')
sleep(2)
print("""{5}Numeros digitados:{6} {0}
{7}Soma de todos os numeros:{6} {1}
Media: {2}
Maior numero: {3}
Menor numero: {4}""".format(cont, soma, (soma/cont), maior, menor, cor['vermelho'], cor['fim'], cor['verde']))
