print('===== DESAFIO 95 =====')
# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

# jogadores = []
#
# while True:
#
#     nome = str(input('Nome do Jogador: '))
#     partidas = int(input(f'Quantas partidas {nome} jogou? '))
#     gols = []
#     for g in range(partidas):
#         gol = int(input(f'Quantos gols na partida {g}? '))
#         gols.append(gol)
#
#     jogador = {'nome': nome, 'gols': gols, 'total_gols': sum(gols)}
#     jogadores.append(jogador)
#
#     resp = str(input('Deseja continuar? [S/N] '))
#     if resp in 'Nn':
#         break
#
# print('-=' * 30)
# print('LEVANTAMENTO DOS JOGADORES:')
# print('-=' * 30)
# print(f'{"cod":<4} {"nome":<20} {"gols":<20} total')
# print('-' * 50)
#
# for cod, jogador in enumerate(jogadores):
#     print(f'{cod:>3} {jogador["nome"]:<20} {jogador["gols"]} {jogador["total_gols"]}')
#
# print('-' * 50)
# dado = int(input('Mostar dado de qual jogador? '))
#
# while dado != 999:
#     dado = int(dado)
#     if dado < len(jogadores):
#         jogador_selec = jogadores[dado]
#         print(f'--- LEVANTAMENTO DO JOGADOR {jogador_selec["nome"]}:')
#         for partida, gol in enumerate(jogador_selec["gols"]):
#             print(f'No jogo {partida} fez {gol} gols.')
#         else:
#             print('Jogador não encontrado.')
#
#         dado = input('Mostrar dado de qual jogador? (Digite 999 para sair).')
# print('--- FIM DO PROGRAMA ---')

print('\n *** Resposta do Professor esta comentado ***')
# Ficou muito mais completo e melhor que foi feito
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')  # daqui até o final do for é o cabeçalho, que tive muita dificuldade de fazer o alinhamento
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dado de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe esse jogador com código {busca}!')
    else:
        print(f' ---LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')
