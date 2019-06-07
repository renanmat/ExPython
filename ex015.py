d = int(input('Digite por quantos dias o carro foi alugado: '))
km = float(input('Digite quantos KM foi rodados: '))
pd = d*60
pkm = km*0.15
print('O preço do carro alugado fica: R${}'.format(pd+pkm))

