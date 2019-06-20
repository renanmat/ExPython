def metade(n, f=False):
    """
    -> funçao que divide o numero por 2.
    :param n: numero para ser dividido.
    :param f: (opcional)formata o resultado para um valor monetario.Ex: R$50,00
    :return: resultado da divizão.
    """
    r = n / 2
    if f:
        return moeda(r)
    else:
        return r


def dobro(n, f=False):
    """
    -> multiplica um valor por 2.
    :param n: numero para ser multiplicado.
    :param f: (opcional)formata o resultado para um valor monetario.Ex: R$50,00
    :return: o dobro de n.
    """
    r = n * 2
    return r if f is False else moeda(r)


def aumentar(n, por, f=False):
    """
    -> aumenta um valor conforme a porcentagem informada.
    :param n: valor para ser aumentado.
    :param por: porcentagem de aumento.
    :param f: (opcional)formata o resultado para um valor monetario.Ex: R$50,00
    :return: o aumento do valor.
    """
    r = (n * por / 100) + n
    if f:
        return moeda(r)
    else:
        return r


def diminuir(n, por, f=False):
    """
    -> Diminui um valor conforme a porcentagem informada.
    :param n: valor para ser diminuido.
    :param por: porcentagem para ser diminuido.
    :param f: (opcional)formata o resultado para um valor monetario.Ex: R$50,00
    :return: resultado da subtraçao.
    """
    r = n - (n * por / 100)
    return r if not f else moeda(r)


def moeda(n):
    """
    -> Formata o valor informado em valores monetarios.
    :param n: valor para ser formatado.
    :return: valor em formato monetario.
    """
    m = f'R${n:.2f}'.replace('.', ',')
    return m


def resumo(p=0, aumento=0, reduçao=0):
    """
    ->Analiza o valor, tranzendo o aumento, a metade, o dobro e a reduçao.
    :param p: valor a ser analizado.
    :param aumento: (opcional) taxa que sera aumentado o valor em %.
    :param reduçao: (opcional) taxa que sera diminuido o valor em %.
    :return: nd.
    """
    print(f'-'*30)
    print(f'Analizado o Valor'.center(30))
    print('-'*30)
    print(f'Analizando o preço \t{moeda(p)}')
    print(f'Metade do preço \t{metade(p, f=True)}')
    print(f'Dobro do preço  \t{dobro(p, f=True)}')
    print(f'Aumento de {aumento:>3}% \t{aumentar(p, aumento, f=True)}')
    print(f'Reduçao de {reduçao:>3}% \t{diminuir(p, reduçao, f=True)}')
