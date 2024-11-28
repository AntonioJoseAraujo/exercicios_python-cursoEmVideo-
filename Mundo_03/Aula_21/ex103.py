print('===== DESAFIO 103 =====')
"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

# def ficha(nome, gol):
#     if nome == '':
#         nome = "<Desconhecido>"
#     if gol == '':
#         gol = 0
#     print('-' * 30)
#     return print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')
#
#
# nome = str(input('Nome do Jogador: '))
# gol = str(input('Número de Gols: '))
# ficha(nome, gol)

print('\n *** Resposta do Professor esta comentado ***')
"""Resposta do professo saiu mais bem elaborado"""


def ficha(jog='<desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
