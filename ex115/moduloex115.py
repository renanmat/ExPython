def escritarq(nome, idade):
    file = open('cadastro.txt', 'w')
    file.write(f'{nome}\t{idade}\n')
    file.close()


def leituarq():
    file = open('cadastro.txt', 'r')
    print(file.read())
    file.close()


def sistcadastro():
    while True:
        print('-'*30)
        print('[1]Novo cadastro')
        print('[2]Lista de pessoas cadastradas')
        print('[3]Sair')
        print('-'*30)
        try:
            resp = int(input('Qual sua opçao? '))
        except:
            print('Erro! Codigo invalido!')
        else:
            if resp == 3:
                break
            elif resp == 1:
                nome = str(input('Nome da pessoa? '))
                idade = int(input('idade? '))
                escritarq(nome, idade)
            elif resp == 2:
                leituarq()
            else:
                print('Opçao invalida.')
