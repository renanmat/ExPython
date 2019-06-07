lista = []
jogos = []
from random import randint
from time import sleep

print('-='*20)
print(f'{"JOGOS DA MEGA SENA":^40}')
print('-='*20)

j = int(input('Quantos jogos voce quer sortear? '))
n = 0
cont = 0
for c in range(0, j):
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont +=1
        if cont >= 6:
            lista.sort()
            jogos.append(lista[:])
            lista.clear()
            break
    cont = 0
print('-='*4, f'Sorteio de {j} jogos', '-='*4)
for i, jogo in enumerate(jogos):
    print(f'{i+1}° jogo: {jogo}')
    sleep(1)
print('-='*5, 'BOA SORTE!', '-='*5)
