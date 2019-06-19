from time import sleep
cores = {'amarelo': '\033[1;30;42m', 'azul': '\033[1;30;44m', 'vermelho': '\033[1;30;41m', 'limpa': '\033[m',
         'branco': '\033[1;7;30m'}


def ModTt(msg, cor='limpa'):
    """
    --> funçao de titulo personalizado com corres.
    :param msg: string com o titulo.
    :param cor: (opcional) cores entre: amarelo, vermelho, azul e branco.
    :return: nd.
    """
    titulo = f"  {msg}  "
    print(f'{cores[cor]}~' * len(titulo))
    print(titulo)
    print('~' * len(titulo), end='\n\033[m')
    sleep(1)


def pyHelp():
    """
    --> sistema de ajuda com o manual das funções e bibliotecas.
    :return: nd.
    """
    while True:
        ModTt('Sistema de Ajuda PyHelp', cor='amarelo')
        pes = str(input('\033[mBiblioteca ou Funçao: ')).strip().lower()
        if pes == 'fim':
            ModTt('Até Logo!', cor='vermelho')
            break
        ModTt(f"Acessando o manual do comando '{pes}'", cor='azul')
        print(cores['branco'])
        help(pes)
        print(cores['limpa'])
        sleep(2)


pyHelp()
