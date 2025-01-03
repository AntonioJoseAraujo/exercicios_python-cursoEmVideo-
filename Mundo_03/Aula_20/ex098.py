print('===== DESAFIO 98 =====')
# Faça um programa que tenha uma função chamada contador(), que recebe três parâmetros:
# início, fim e passo
# E realize a contagem
# Seu programa tem que realizar três contagens através da função criada
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) Uma contagem personalizada
# --> print(f"{valor} ", end="")  # Exemplo de print espaçado

from time import sleep

# def contador():
#     print('-=' * 30)
#     print('Contagem de 1 até 10 de 1 em 1.')
#     for c in range(1, 11):
#         sleep(0.5)
#         print(f'{c} ', end='')
#     print('FIM!')
#     print('-=' * 30)
#     print('Contagem de 10 até 0 de 2 em 2.')
#     for v in range(10, -1, -2):
#         sleep(0.5)
#         print(f'{v} ', end='')
#     print('FIM!')
#     print('-=' * 30)
#     print('Agora é a sua vez de personalizar o contagem.')
#     i = int(input('Início: '))
#     f = int(input('Fim: '))
#     p = int(input('Passo: '))
#
#     if p == 0:
#         p = 1
#     elif p < 0:
#         p = -p
#     print('-=' * 30)
#     print(f'Contagem de {i} até {f} de {p} em {p}')
#     if i > f:
#         for c in range(i, f - 1, -p):
#             sleep(0.5)
#             print(f'{c} ', end='')
#     else:
#         for c in range(i, f + 1, p):
#             sleep(0.5)
#             print(f'{c} ', end='')
#
#     print('FIM!')
#
#
# contador()

print('\n *** Resposta do Professor esta comentado ***')


# Resposta do professor ficou muito mais bem elaborada


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
