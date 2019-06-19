dados = dict()
dados['nome'] = str(input('Nome do Jogador? '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
dados['gols'] = list()
for cont in range(dados['partidas']):
    dados['gols'].append(int(input(f'Quantos gols na partida {cont}? ')))
dados['total'] = sum(dados['gols'])
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogol {dados["partidas"]}:')
for partida, gol in enumerate(dados['gols']):
    print(f'    =>Na partida {partida}, fez {gol} gols.')
