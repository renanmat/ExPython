maiorid = 0
somaidade = 0
menosde20 = 0
maisvelho = ''
for pess in range(1, 5):
    print('{:-^40}'.format('{}ª pessoa'.format(pess)))
    nome = str(input('Digite o nome: '.format(pess))).strip().upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).strip().upper()
    somaidade += idade
    if idade > maiorid and sexo == 'M':
        maiorid = idade
        maisvelho = nome
    elif idade < 20 and sexo == 'F':
            menosde20 += 1
print("{:-^40}".format('Analizando os dados'))
print('A media de idade das pessoas é {} anos'.format(somaidade/pess))
print('O nome do homem mais velho é {}'.format(maisvelho))
print('E tem {} mulheres menos de 20 anos'.format(menosde20))
print('-'*40)
