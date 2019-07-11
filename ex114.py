import requests
try:
    r = requests.get('http://pudim.com.br/')
except:
    print('\033[1;31mErro!O site budim nao pode ser acessado!\033[m')
else:
    print('\033[1;32mSite Budim esta acessivel!\033[m')


