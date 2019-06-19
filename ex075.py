palavras = ('carro', 'loja', 'poder', 'perder', 'miniatura', 'bimbolim', 'jovem', 'carta', 'curto', 'joalheria')
for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} tem as vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
