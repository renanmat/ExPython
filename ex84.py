pessoas = list()
dados = []
maisp = menosp = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    op = str(input('quer continuar?[S/N]'))
    if op in 'Nn':
        break
print(f'foram cadastradas {len(pessoas)} pessoas!')

for cont, pes in enumerate(pessoas):
    if cont == 0:
        maisp = menosp = pes[1]
    else:
        if pes[1] > maisp:
            maisp = pes[1]
        elif pes[1] < menosp:
            menosp = pes[1]

print(f'O maior peso foi {maisp} Kg de:', end=' ')
for pes in pessoas:
    if maisp in pes:
        print(pes[0], end='...')

print(f'\nE o menor peso foi {menosp} Kg de :', end=' ')
for pes in pessoas:
    if menosp in pes:
        print(pes[0], end='...')


