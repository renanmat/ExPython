def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero. Ex: 5 x 4 x 3 x 2 x 1 = 120
    :param num: Numero para calculo.
    :param show:(opcional) Mostra o calculo.
    :return: retorna o resultado fatorial.
    """
    f = 1
    for cont in range(num, 0, -1):
        f *= cont
        if show:
            if cont != 1:
                print(cont, end=' x ')
            else:
                print(cont, end=' = ')
    return f


print(fatorial(5, show=True))
help(fatorial)
