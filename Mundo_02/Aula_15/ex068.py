print('===== DESAFIO 68 =====')
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

computador = randint(0, 10)
cont = 0

print('===== Vamos Jogar Par ou Ímpar =====')
while True:
    print(computador)
    jogador = int(input('Digite um valor: '))
    op = str(input('Você quer PAR ou ÍMPAR? [P/I] ')).upper().strip()[0]
    soma = jogador + computador
    res = ''

    print('-' * 30)
    if soma % 2 == 0:
        res = 'DEU PAR!'
        print(f'Você jogou {jogador} e o Computador jogou {computador}. Total de {soma} {res}.')
        print('-' * 30)
        if op == 'P':
            cont += 1
            print('Você Venceu!')
            print('Vamos jogar novamente...')
            print('-' * 30)
        else:
            print('PERDEU!')
            break
    if soma % 2 != 0:
        res = 'DEU ÍMPAR'
        print(f'Você jogou {jogador} e o Computador jogou {computador}. Total de {soma} {res}.')
        print('-' * 30)
        if op == 'I':
            cont += 1
            print('Você Venceu!')
            print('Vamos jogar novamente...')
            print('-' * 30)
        else:
            print('PERDEU!')
            break
print('-=' * 30)

print(f'GAME OVER!!!. Você venceu {cont} vezes.')

print('\n *** Resposta do Professor esta comentado ***')

# v = 0
# while True:
#     jogador = int(input('Diga um valor: '))
#     computador = randint(0, 10)
#     total = jogador + computador
#     tipo = ' '
#     while tipo not in 'PI':
#         tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
#     print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
#     print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
#     if tipo == 'P':
#         if total % 2 == 0:
#             print('Você VENCEU!')
#             v += 1
#         else:
#             print('Você PERDEU!')
#             break
#     elif tipo == 'I':
#         if total % 2 == 1:
#             print('Você VENCEU!')
#             v += 1
#         else:
#             print('Você PERDEU!')
#             break
#     print('Vamos jogar novamente...')
# print(f'GAME OVER! Você venceu {v} vezes.')
