def notas(*num, sit=False):
    """
    -> analiza nostas de um aluno.
    :param num: notas do aluno(sem limite de quantidade)
    :param sit: (opcional) mostra a situaçao em que o aluno ficou de acordo com a media.
    :return: Biblioteca com o total de notas, a média, a maior, menor nota e situaçao do aluno(opcional).
    """
    ana = dict()
    ana['total'] = len(num)
    for p, c in enumerate(num):
        if p == 0:
            maior = menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
    ana['maior'] = maior
    ana['menor'] = menor
    ana['media'] = sum(num)/len(num)
    if sit:
        if ana['media'] < 6:
            ana['Situaçao'] = 'ruim'
        elif ana['media'] < 7:
            ana['Situaçao'] = 'razoavel'
        else:
            ana['Situaçao'] = 'boa'
    return ana


resp = notas(6, 7, 5.2, sit=True)
print(resp)
