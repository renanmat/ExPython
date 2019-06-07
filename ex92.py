from datetime import date
dados = dict()
dados['nome'] = str(input('Digite o nome: '))
dados['ano'] = int(input('Digite o ano de nascimento: '))
dados['ctps'] = int(input('Digite o nº da carteira de trabalho: '))
dados['idade'] = date.today().year - dados['ano']
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Ano de contrataçao: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = (dados['contrataçao'] - dados['ano']) + 35
print('-='*25)
for k, v in dados.items():
    print(f'-{k} tem o valor {v}')
