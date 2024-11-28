print('===== DESAFIO 111 =====')
"""
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.
"""

# from utilidadesCeV.moeda import resumo
# No import abaixo foi feito pelo professor que importa todos os módulos
from Mundo_03.Aula_22.ex111.utilidadesCeV import moeda

p = float(input('Digite o preço: R$ '))
# resumo(p, 75, 15)
moeda.resumo(p, 35, 22)

print('\n *** Resposta do Professor esta comentado ***')
# Professor fez um import no INIT das utilidades para utilizar todos os módulos
