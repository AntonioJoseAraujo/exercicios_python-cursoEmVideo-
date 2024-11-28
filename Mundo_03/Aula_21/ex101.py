print('===== DESAFIO 101 =====')
"""
Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""
from datetime import date

# def voto(idade):
#     if idade < 18:
#         return print(f'Com {idade} anos: NÃO VOTA.')
#     elif idade >= 65:
#         return print(f'Com {idade} anos: VOTO OPCIONAL.')
#     elif idade >= 18:
#         return print(f'Com {idade} anos: VOTO OBRIGATÓRIO. ')
#
#
# # Programa Principal
# ano_nasc = int(input('Em que ano você nasceu? '))
# idade = date.day().year - ano_nasc
# voto(idade)

print('\n *** Resposta do Professor esta comentado ***')
'''Professor informou que com essa forma tem melhor desenho no código ja que a grande maioria do código referente a idade fica diretamente no def voto'''


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
