from random import randint
from operator import itemgetter
from time import sleep
sorteio = {'jogador1': '',
           'jogador2': '',
           'jogador3': '',
           'jogador4': ''}
ranking = dict()
print('Sorteio:')
for gamer in sorteio:
    sorteio[gamer] = randint(1, 6)
    print(f'{gamer} tirou {sorteio[gamer]} no dado.')
    sleep(1)
print('-='*15)

ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)

print(f'{"== Ranking ==":^25}')
for k, v in enumerate(ranking):
    print(f' {k+1} lugar {v[0]} com {v[1]}')
    sleep(1)
