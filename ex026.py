f = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {} veses na frase'.format(f.count('a')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(f.find('a')+1))
print('A letra "A" aparece pela ultima vez na posição {}'.format(f.rfind('a')+1))

