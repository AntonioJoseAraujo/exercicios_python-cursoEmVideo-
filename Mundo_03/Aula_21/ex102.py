print('===== DESAFIO 102 =====')
"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(n, show=False):
    '''
    -> Calcúla o Fatorial de um número.
    :param n: O número que vai ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor Fatorial de um número n.
    '''
    f = 1
    print('-' * 30)
    for i in range(n, 0, -1):
        if show:
            print(f'{i}', end=' ')
            if i > 1:
                print(f'x', end=' ')
            else:
                print(f'=', end=' ')
        f *= i
    return f


print(fatorial(5, True))
print('-' * 30)
help(fatorial)

print('\n *** Resposta do Professor esta comentado ***')
'''Resposta do professor foi igual'''
