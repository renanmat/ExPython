def voto(nasc):
    """
    -> funçao que calcula a idade e responde se o cidadao tem voto obrigatorio, opcional ou negado.
    :param nasc: recebe o ano de nacimento do usuario.
    :return: retorna com a idade e a condiçao do eleitor.
    """
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        resp = 'Negado'
    elif 18 <= idade < 70:
        resp = 'Obrigatorio'
    else:
        resp = 'Opcional'
    return f'Sua idade é {idade} anos voto: {resp}'


a = int(input('Ano de nascimento? '))
print(voto(a))
