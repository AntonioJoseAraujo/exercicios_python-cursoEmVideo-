print('===== DESAFIO 91 =====')
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

# Não consegui terminar e não foi feito =(

from random import randint
from time import sleep
from operator import itemgetter  # para colocar em ordem é preciso importar essa biblioteca

jogo = {'jogador1': randint(1, 6),
        'jogodor2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(
    1),
                 reverse=True)  # se colocar o valor 0 vai aparecer os (jogadores) mais colocando o 1 como esta vai aparecer os resultados do randint
print('-=' * 30)
print(' === RANKING DOS JOGADORES ===')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
