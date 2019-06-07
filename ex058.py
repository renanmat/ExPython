from random import randint
comp = 1
user = 0
cont = 0
while comp != user:
    comp = randint(0, 10)
    user = int(input('Em qual numero o computador pensou? '))
    print('Computador pensou no numero {}.'.format(comp))
    if user == comp:
        print('Parabens! voce acertou!')
    else:
        print('Voce errou! Tente novamente.')
    cont += 1
print('Fim de jogo! Voce teve que tentar {} vezes até acertar.'.format(cont))
