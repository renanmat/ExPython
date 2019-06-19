lista = []

while True:
    aluno = str(input('aluno: ')).strip()
    nota1 = float(input('1° nota: '))
    nota2 = float(input('2° nota: '))
    media = ((nota1 + nota2) / 2)
    lista.append([aluno, [nota1, nota2], media])
    op = str(input('Quer continuar?[S/N] '))[0].strip()
    if op in 'nN':
        break
print('-='*5, 'Medias', '-='*5)
for a in lista:
    print(f'{a[0]:<10} ---- {a[2]:^5}')
print('-='*14)

while True:
    print('notas [999 para sair!]')
    al = str(input('Aluno: '))
    if al != '999':

        for a in lista:
            if al in a:
                print('-=' * 5, 'Notas', '-=' * 5)
                print(f'{a[0]} -- 1° {a[1][0]} -- 2° {a[1][1]}')
                print('-='*14)
                break
    else:
        break
