n = int(input('Digite um numero para ver seu fatorial: '))
cont = 1
mult = 1
while cont <= n:
    mult = mult * cont
    cont += 1
print('{}! = {}'.format(n, mult))
