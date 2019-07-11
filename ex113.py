def leiaInt(prompt=''):
    """
    -> le apenas numero inteiro.
    :param prompt: texto para o usuario.
    :return: apenas numeros inteiro.
    """
    while True:
        try:
            num = int(input(prompt))
        except KeyboardInterrupt:
            print('Nenhum numero foi digitado!')
            num = 0
            break
        except ValueError:
            print('\033[1;31mErro! Digite um numero interio valido.\033[m')
        else:
            break
    return num


def leiaFloat(prompt=''):
    """
    -> le apenas numeros reais.
    :param prompt: texto para usuario.
    :return: numero inteiro.
    """

    while True:
        try:
            num = float(input(prompt))
        except KeyboardInterrupt:
            print('Nenhum numero foi digitado!')
            num = 0
            break
        except:
            print('Erro! Digite um numero Real valido.')
        else:
            break
    return num


n = leiaInt('Digite um numero inteiro: ')
f = leiaFloat('Digite um numero real: ')
print(f'Numero Interio {n} e numero Real {f} ')
