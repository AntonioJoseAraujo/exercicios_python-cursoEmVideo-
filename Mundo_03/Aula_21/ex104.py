print('===== DESAFIO 104 =====')
"""
Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
ex.:
n = leia_int("Digite um n")
"""

# def leiaInt(msg):
#     n = input(msg)
#     while not n.isdigit():
#         print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
#         n = input(msg)
#     return int(n)
#
#
# # Programa Principal
# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}.')

print('\n *** Resposta do Professor esta comentado ***')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;33mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
