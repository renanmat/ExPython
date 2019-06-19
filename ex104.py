def leiaInt(prompt=''):
    """
    -> le apenas numero inteiro.
    :param prompt: texto para o usuario.
    :return: apenas numeros inteiro.
    """
    ok = False
    while True:
        nun = input(prompt)
        if nun.isnumeric():
            ok = True
        else:
            ok = False
            print('\033[1;31mErro! Digite um numero.\033[m')
        if ok:
            break
    return int(nun)


n = leiaInt('Digite um numero: ')
print(f'O numero digitado foi {n} ')
print(type(n))
