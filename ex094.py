dados = dict()
pessoas = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome? ')).strip().lower()
    dados['sexo'] = str(input('sexo[M/F]? '))[0].strip().lower()
    if dados['sexo'] not in 'mf':
        print('Erro! Responda somente M ou F.')
        dados['sexo'] = str(input('sexo? '))[0].strip().lower()
    dados['idade'] = int(input('Idade? '))
    pessoas.append(dados.copy())
    op = str(input('Quer continuar[S/N]? '))[0].strip().lower()
    if op not in 'sn':
        print('ERRO! Responda S ou N.')
        op = str(input('Quer continuar[S/N]? '))[0].strip().lower()
    if op in 'Nn':
        break
print('-='*25)

print(f'A) ao todo temos {len(pessoas)} pessoas cadastradas.')
soma = 0
for dado in pessoas:
    soma += dado['idade']
media = soma / len(pessoas)
print(f'B) A media de idades é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for pes in pessoas:
    f = pes['sexo']
    if f == 'f':
        print(pes['nome'], end=' ')
print()
print(f'D) Lista de pessoas que estao acima da media:')
for pes in pessoas:
    idade = pes['idade']
    if idade > media:
        for k, v in pes.items():
            print(f'    {k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
