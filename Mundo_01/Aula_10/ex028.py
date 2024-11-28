print('===== DESAFIO 28 =====')
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.


from random import randint

pc = randint(0, 5)
# print(pc) # verificando o random
user = int(input('Tente descobrir qual foi o número escolhido pelo PC, entre 0 e 5: '))

if pc == user:
    print('Você Venceu!')
else:
    print('Você Perdeu!')

# ------------------------------------
print('\n--- Resolução pelo Professor esta comentada ---')
# from random import randint
# from time import sleep
#
# computador = randint(0, 5)  # Faz o computador "PENSAR"
# print('-=-' * 20)
# print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
# print('-=-' * 20)
# jogador = int(input('Em que número eu pensei? '))  # Jogador tenta advinhar
# print('PROCESSANDO...')
#
# sleep(3)
# if jogador == computador:
#     print('PARABÉNS! Você conseguiu me vencer!')
# else:
#     print('Você PERDEU! Eu pensei no número {} e não no {}!'.format(computador, jogador))
