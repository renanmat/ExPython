sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual é seu sexo(M/F)? ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido! Digite novamente:')
print('Obrigado!!')