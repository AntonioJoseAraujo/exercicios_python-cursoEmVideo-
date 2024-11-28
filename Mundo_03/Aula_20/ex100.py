print('===== DESAFIO 100 =====')
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

#
#
# def sorteia():
#     print(f'Sorteando 5 valores da lista: {num} PRONTO!')
#
#
# def soma_par():
#     print(f'Somando os valores pares de {num}, temos {soma}.')
#
#
# # Programa principal
# num = list()
# soma = 0
# for c in range(0, 5):
#     n = randint(1, 10)
#     num.append(n)
#     if n % 2 == 0:
#         soma += n
#
# sorteia()

print('\n *** Resposta do Professor esta comentado ***')


# Ficou mais bem elaborado


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
        print(f'Somando os valores pares de {lista}, temos {soma}.')


números = list()
sorteia(números)
somaPar(números)
