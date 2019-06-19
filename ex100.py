from random import randint


def soma(lista):
    somapar = 0
    for n in lista:
        if n % 2 == 0:
            somapar += n
    print(f'A soma dos numeros pares {lista} é igual a {somapar}.')


def sortlista(lista):
    """
    -> Sorteia 5 numeros de 0 até 10, depois coloca em uma lista.
    :param lista: lista para receber os numeros sorteados.
    :return: sem retorno.
    """
    for cont in range(0, 5):
        lista.append(randint(0, 10))

    print(f'Sorteando 5 valores da lista:', end=' ')
    for cont in lista:
        print(f'{cont}', end=' ')
    print(f'fim')


# Programa principal
numeros = list()
sortlista(numeros)
soma(numeros)

help(sortlista)
