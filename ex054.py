from datetime import date
maior = 0
menor = 0
for cont in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(cont)))
    idade = date.today().year - ano
    print('{} anos'.format(idade))
    if idade > 21:
        maior += 1
    else:
        menor += 1
print('Maior de idade: {}'.format(maior))
print('Menor de idade: {}'.format(menor))
