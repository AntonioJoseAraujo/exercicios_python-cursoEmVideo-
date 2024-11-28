print('===== DESAFIO 88 =====')
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.

from random import randint
from time import sleep

# Não consegui fazer

# print('=' * 50)
# print(f'{'Palpiteiro: MEGA SENA':^50}')
# print('=' * 50)
#
# listas = list()
# jogos = list()
# qtdade = int(input('Quantos jogos você quer que eu sorteie? '))
# cont = 1
# while cont <= qtdade:
#
#     n = randint(1, 60)
#     if n not in listas:
#         listas.append(n)
#     if jogos == 0:
#         break
#     listas.sort()
#     jogos.append(listas[:])
#     listas.clear()
# print(listas)

print('\n *** Resposta do Professor esta comentado ***')

lista = list()
jogos = list()
cont = 0
print('-' * 30)
print('     Joga na Mega Sena     ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
