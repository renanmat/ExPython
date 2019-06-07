print('Progressao Aritimetica (P.A)')
pt = int(input('Ditite o primeiro termo: '))
r = int(input('Digite a razão: '))
a10 = pt + (10 - 1)*r
print('Os 10 primeiros termos sao:')
for c in range(pt, a10+1, r):
    print('{}'.format(c), end=' -> ')
print('Fim')