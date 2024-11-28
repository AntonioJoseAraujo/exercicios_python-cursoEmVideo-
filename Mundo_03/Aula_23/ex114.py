print('===== DESAFIO 114 =====')
'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
# Não conseguir fazer
print('\n *** Resposta do Professor esta comentado ***')
'''Não acessou o site Pudim, porém para outros site como youtube ele acessou. Então não esta errado, só ñ funciono no site pudim '''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site não está acessível no momento.')
else:
    print(f'Consegui acessar o site com sucesso!')
    # print(site.read()) # aqui ele pega todo o código do site
