from time import sleep


def contador(inicio, fim, passo):
    if inicio > fim:
        sig = -1
    else:
        sig = 1
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = passo * -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    for cont in range(inicio, fim + sig, passo * sig):
        print(cont, end=' ')
        sleep(0.5)
    print(f'FIM')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Personalize a contagem: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
