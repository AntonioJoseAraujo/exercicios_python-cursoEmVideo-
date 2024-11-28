print('===== DESAFIO 58 =====')
# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint
from time import sleep

palpite = 1
jogar = str(input('Vamos jogar? [S/N] ')).upper().strip()
while jogar == 'S':
    computador = randint(0, 10)  # Faz o computador "PENSAR"
    print('-=-' * 20)
    print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
    print('-=-' * 20)
    print(computador)
    jogador = int(input('Em que número eu pensei? '))  # Jogador tenta advinhar
    print('PROCESSANDO...')
    print('-=-' * 20)

    sleep(1)
    if jogador != computador:
        print('Você PERDEU! Eu pensei no número {} e não no {}!'.format(computador, jogador))
        palpite += 1
    else:
        jogar = 'n'
        print('PARABÉNS! Você conseguiu me vencer!')
        print('Você tentou {} vezes.'.format(palpite))

print('\n *** Resposta do Professor esta comentado ***')

# from random import randint
#
# computador = randint(0, 10)
# print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
# print('Será que você consegue advinhar qual foi? ')
# acertou = False
# palpite = 0
# while not acertou:
#     jogador = int(input('Qual é seu palpite? '))
#     palpite += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print('Mais... Tente mais uma vez.')
#         elif jogador > computador:
#             print('Menos... Tenta mais uma vez.')
# print('Acertou com {} tentativas. Parabéns!'.format(palpite))
