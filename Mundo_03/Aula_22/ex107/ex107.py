print('===== DESAFIO 107 =====')
"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas 'aumentar()', 'diminuir()', 'dobro()' e 'metade()'.
Faça também um programa que importe esse módulo e use algumas dessas funções.
Obs.: por exemplo, o 'aumentar()' recebe o preço e uma porcentagem, e calcula o 'diminuir()', mesma coisa.
"""
# Caso esteja sublinhado podemos fazer ese tipo de import especificando todo o caminho
# from Mundo_03.Aula_22.ex107 import moeda

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')

print('\n *** Resposta do Professor esta comentado ***')
'''Resposta do professor foi igual, mudando somente o nome da variavel dentro do moeda'''
