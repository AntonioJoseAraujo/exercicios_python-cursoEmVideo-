print('=====  DESAFIO 71 =====')
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# print('=' * 30)
# print('--- Banco do T ---')
# print('=' * 30)
# # 1234
# saque = int(input('Qual o valor você quer sacar? R$ '))
# maior_nota = 50
# total_notas = 0
#
# while True:
#     if saque >= maior_nota:
#         saque -= maior_nota
#         total_notas += 1
#     else:
#         if total_notas > 0:
#             print(f'Total de {total_notas} cédulas de R${maior_nota:.2f}')
#         if maior_nota == 50:
#             maior_nota = 20
#         elif maior_nota == 20:
#             maior_nota = 10
#         elif maior_nota == 10:
#             maior_nota = 5
#         elif maior_nota == 5:
#             maior_nota = 2
#         elif maior_nota == 2:
#             maior_nota = 1
#         total_notas = 0
#
#         if saque == 0:
#             break
# print('=' * 30)
# print('Volte sempre ao Banco T! Tenha um bom dia!')
# print('=' * 30)

print('\n *** Resposta do Professor esta comentado ***')

print('=' * 30)
print('{:^30'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
