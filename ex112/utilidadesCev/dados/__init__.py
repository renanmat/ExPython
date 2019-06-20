def LeiaDinheiro(msg):
    while True:
        ok = False
        men = input(msg).strip()
        if not men.isalpha() and not men == '' and not men.isalnum():
            ok = True
        else:
            print('\033[1;31mErro! Digite um numero valido.\033[m')
        if ok:
            break
    return float(men.replace(',', '.'))

