print('===== DESAFIO 113 =====')
"""Reescreva a função `leiaInt()` que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também a função `leiaFloat()` com a mesma funcionalidade."""

# def leiaInt(msg):
#     ok = False
#     valorInt = 0
#     while not ok:
#         try:
#             n = str(input(msg)).strip()
#             if n.isnumeric():
#                 valorInt = int(n)
#                 ok = True
#             else:
#                 print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
#         except (ValueError, TypeError):
#             print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
#         except KeyboardInterrupt:
#             print('\n\033[0;33mO usuário preferiu não informar esse valor!\033[m')
#             return 0
#         except Exception as error:
#             print(f'O erro encontrado foi {error.__class__}')
#             print(f'O erro encontrado foi {error.__cause__}')
#     return valorInt
#
#
# def leiaFloat(msg):
#     ok = False
#     valorFlo = 0.0
#     while not ok:
#         try:
#             n = str(input(msg)).strip()
#             valorFlo = float(n)
#             ok = True
#
#         except ValueError:
#             print('\033[0;31mERRO! Digite um número real válido.\033[m')
#         except KeyboardInterrupt:
#             print('\n\033[0;33mO usuário preferiu não informar esse valor!\033[m')
#             return 0
#         except Exception as error:
#             print(f'O erro encontrado foi {error.__class__}')
#             print(f'O erro encontrado foi {error.__cause__}')
#     return valorFlo
#
#
# num = leiaInt('Digite um número INTEIRO: ')
# numF = leiaFloat('Digite um número REAL: ')
# print(f'O valor inteiro foi {num} e o real foi {numF}.')

print('\n *** Resposta do Professor esta comentado ***')
'''Resposta do professor ficou melhor'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número inteiro válido!\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número real válido!\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')
