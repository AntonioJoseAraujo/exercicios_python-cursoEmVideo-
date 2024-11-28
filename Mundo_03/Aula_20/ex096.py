print('===== DESAFIO 96 =====')


# Faça um programa que tenha uma função chamada area(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

def area(l, c):
    print('-' * 30)
    print('Controle do Terreno')
    print('=' * 30)
    a = c * l
    print(f'A área de um terreno de {l} x {c} é de {a}m²')


# Programa Principal
largura = float(input('Largura: (m) '))
comprimento = float(input('Comprimento: (m) '))
area(largura, comprimento)

print('\n *** Resposta do Professor esta comentado ***')
'''A resposta do professor foi praticamente igual'''
