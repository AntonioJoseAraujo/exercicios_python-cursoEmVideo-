print('===== DESAFIO 106 =====')
"""
Faça um mini sistema que utilize o interactive help do Python
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o programa se encerrará!.
OBS: use cores.
"""
from time import sleep

# cores = {'limpa': '\033[m',
#          'azul': '\033[1;30;44m',
#          'branco': '\033[7;40m',
#          'vermelho': '\033[1;30;41m',
#          'verde': '\033[1;42m'}
#
# while True:
#
#     print(f'{cores['verde']}~' * 50)
#     print(f'{'SISTEMA DE AJUDA PyHELP':^50}')
#     print(f'~' * 50)
#     resp = str(input(f'{cores['limpa']}Função ou Biblioteca > ')).lower()
#
#     print(f'{cores['azul']}~' * 40)
#     print(f'Acessando o manual do comando "{resp}" ...')
#     print('~' * 40)
#     print(f'{cores['limpa']}')
#     sleep(1)
#     print(f'{cores['branco']}')
#     help(f'{resp}')
#     print(f'{cores['limpa']}')
#     if resp == 'fim':
#         sleep(1)
#         print(f'{cores['vermelho']}~' * 10)
#         print(f'{'ATÉ LOGO!'}', flush=True)
#         print(f'~' * 10)
#         print(f'{cores['limpa']}')
#         break
#

print('\n *** Resposta do Professor esta comentado ***')
c = ('\033[m',  # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m'  # 6 - branco
     );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    sleep(1)


# Programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
