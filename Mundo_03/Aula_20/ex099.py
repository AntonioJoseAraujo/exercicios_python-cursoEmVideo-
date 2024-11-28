print('===== DESAFIO 99 =====')

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# def maior(*num):
#     print('-=' * 30)
#     print('Analisando os valores passados...')
#     if num is None:
#         print(f'Foram informados 0 valores ao todo.')
#         print(f'O maior valor informado foi o 0.')
#     print(f'{num} Foram informados {len(num)} valores ao todo.')
#     print(f'O maior valor informado foi o {max(num)}.')
#
#
# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()

print('\n *** Resposta do Professor esta comentado ***')
from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todos.')
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 4)
maior(6)
maior()
