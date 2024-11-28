print('===== DESAFIO 112 =====')
"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dado para aceitar apenas valores que sejam monetários.
"""

from utilidadesCeV import moeda
from utilidadesCeV import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 75, 15)

print('\n *** Resposta do Professor esta comentado, no init de dado ***')
