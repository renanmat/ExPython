def ficha(jog='<desconhecido>', gols=0):
    """
    -> mostra o nome do jogador e quantidade de gols.
    :param jog: (opcional) nome do jogador.
    :param gols: (opcional) quantidade de gols.
    :return: nada.
    """
    print(f'O jogador {jog} fez {gols} gols.')


nome = str(input('Nome do jogador? ')).strip()
g = str(input('Gols marcados? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome == '':
    ficha(gols=g)
else:
    ficha(nome, g)
help(ficha)
