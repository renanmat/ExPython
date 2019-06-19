numero = (
    'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
    'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = ''
    n = int(input('Digite um numero: '))
    if n < 0:
        break
    print(f'voce digitou o numero {numero[n]}')
