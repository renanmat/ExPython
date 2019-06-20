def metade(n):
    r = n / 2
    return r


def dobro(n):
    r = n * 2
    return r


def aumentar(n, por):
    r = (n * por / 100) + n
    return r


def diminuir(n, por):
    r = n - (n * por / 100)
    return r


def moeda(n):
    m = f'R${n:.2f}'.replace('.', ',')
    return m
