dados = dict()
jogadores = list()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do Jogador? '))
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    dados['gols'] = list()
    for cont in range(dados['partidas']):
        dados['gols'].append(int(input(f'Quantos gols na partida {cont+1}? ')))
    dados['total'] = sum(dados['gols'])
    jogadores.append(dados.copy())
    while True:
        resp = str(input('Quer continuar[S/N]? ')).strip().lower()[0]
        if resp in 'sn':
            break
        print('Erro! Responda apenas S ou N.')
    if resp in 'n':
        break
print('-='*30)
print(f'{"Cod"} ', end='')
for k in jogadores[0].keys():
    print(f'{k:<15}', end='')
print()
print('-' * 60)
for pos, jog in enumerate(jogadores):
    print(f'{pos:<3}', end=' ')
    for d in jog.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*60)
while True:
    cod = int(input('Mostrar dados de qual jogador?(999 para sair) '))
    if cod == 999:
        print('<< Fim do Programa! >>')
        break
    if cod >= len(jogadores):
        print(f'ERRO! Nao existe jogador com codigo {cod}!')
    else:
        print(f' --Levantamento do jogador {jogadores[cod]["nome"]}')
        for pos, v in enumerate(jogadores[cod]['gols']):
            print(f'    No jogo {pos+1} fez {v} gols.')
    print('-'*60)
