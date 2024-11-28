print('===== DESAFIO 73 =====')
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em
# que posição está o time da São Paulo.

time = (
    'Flamengo', 'Botafogo', 'Palmeiras', 'Fortaleza', 'Cruzeiro', 'São Paulo', 'Bahia', 'Athletico-PR', 'Atlético-MG',
    'Red Bull Bragantino', 'Vasco', 'Criciúma', 'Juventude', 'Internacional-AL', 'Corinthians', 'Grêmio', 'Vitória',
    'Cuiabá', 'Fluminense', 'Atlético-GO')
print(f'Lista de times do Brasileirão: {time}')
print('-=' * 30)
print(f'Os 5 primeiros são {time[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {time[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-=' * 30)
print(f'O São Paulo está na {time.index('São Paulo') + 1}ª posição.')

print('\n *** Resposta do Professor foi exatamente igual ***')
