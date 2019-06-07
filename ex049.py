m = int(input('Qual tabuada voce deseja ver? '))
print('{:-^20}'.format(' TABUADA DO {} '.format(m)))
for cont in range(1, 11):
    r = m * cont
    print('{:5}  x {:>2} = {:>2}'.format(m, cont, r))
print('-'*20)
