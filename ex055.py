maior = 0
menor = 0
for cont in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa em Kg: '.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('A pessoa com maior peso tem {:.2f}Kg'.format(maior))
print('A pessoa com menor peso tem {:.2f}Kg'.format(menor))
