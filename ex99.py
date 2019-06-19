from time import sleep


def maior(* num):
    print('Analizando valores...')
    m = 0
    for p, cont in enumerate(num):
        print(f'{cont}', end=' ')
        sleep(1 / 2)
        if p == 0:
            m = cont
        else:
            if cont > m:
                m = cont
    print(f'Foram analizados {len(num)} numeros ao todo')
    print(f'O maior numero é {m}')
    print('-='*30)


# Programa Principal
maior(20, 12, 9, 5, 14)
maior(6, 1)
maior(2, 5, 3, 1)
maior(7)
maior()
