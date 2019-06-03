from time import sleep

print('Contagem regressiva...')
for cont in range(10, -1, 0 - 1):
    print(cont)
    sleep(1)
print('\033[1;30;41mBOOOOOOOOOOOM!!!!\033[m')
