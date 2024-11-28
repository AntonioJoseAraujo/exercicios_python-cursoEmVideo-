print('===== DESAFIO 45 =====')
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

# computado = randint(1, 3)
# player = int(input(' -==- JOKENPÔ -==-\n'
#                    'Vamos começar com o jogo.\n'
#                    '[1] - Pedra \n'
#                    '[2] - Papel\n'
#                    '[3] - Tesoura\n'
#                    'Faça sua escolha: '))
#
# if player == 1:
#     print('\nVocê escolheu PEDRA')
# elif player == 2:
#     print('\nVocê escolheu PAPEL')
# else:
#     print('\nVocê escolheu TESOURA')
# if computado == 1:
#     print('O PC escolheu PEDRA')
# elif computado == 2:
#     print('O PC escolheu PAPEL')
# else:
#     print('O PC escolheu TESOURA')
#
# if player == 1:  # Player Pedra
#     if computado == 1:
#         print('Ninguém ganhou.')
#     elif computado == 2:
#         print('Você PERDEU!')
#     elif computado == 3:
#         print('Você GANHOU!')
# elif player == 2:  # Player Papel
#     if computado == 1:
#         print('Você GANHOU!.')
#     elif computado == 2:
#         print('Ninguém ganhou.')
#     elif computado == 3:
#         print('Você PERDEU!')
# elif player == 3:  # Player Tesoura
#     if computado == 1:
#         print('Você PERDEU!')
#     elif computado == 2:
#         print('Você GANHOU!')
#     elif computado == 3:
#         print('Ninguém ganhou.')

print('\n----- Resolução do Professor esta comentada -----')
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
 [0] PEDRA
 [1] PAPEL
 [2] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
