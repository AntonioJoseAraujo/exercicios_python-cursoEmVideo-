print('===== DESAFIO 93 =====')
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

# jogador = {}
# gols = []
# totgols = 0
# jogador['nome'] = str(input('Nome do Jogador: '))
# partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
# for g in range(partidas):
#     gols.append(int(input(f'    Quantos gols na partida {g}? ')))
#     jogador['gols'] = gols
#     jogador['total'] = sum(gols)
#
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
#
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}.')
# print('-=' * 30)
# print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
# for c, g in enumerate(gols):
#     print(f' => Na partida {c}, fez {g} gols.')
# print(f'Foi um total de {jogador['total']} gols.')

print('\n *** Resposta do Professor esta comentado ***')
# Teve pouca coisa de diferente em comparação ao que foi feito
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
