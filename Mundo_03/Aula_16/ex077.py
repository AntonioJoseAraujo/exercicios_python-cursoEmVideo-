print('===== DESAFIO 77 =====')
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

# palavras = ('aprender', 'python', 'estudar', 'livro', 'notebook', 'caneta', 'cafe')
#
# for i, vogais in enumerate(palavras):
#
#     print(f'\nNa palavra {palavras[i].upper()} temos ', end='')
#     for letra in vogais:
#         if letra in 'aeiou':
#             print(f'{letra.lower()} ', end='')

# FOI MUITO DIFICIL... Tive que visualizar respostas para entender como fazer.

print('\n *** Resposta do Professor esta comentado ***')

palavras = ('aprender', 'python', 'estudar', 'livro', 'notebook', 'caneta', 'cafe')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
