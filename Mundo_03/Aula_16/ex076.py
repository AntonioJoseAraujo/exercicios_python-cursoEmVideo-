print('===== DESAFIO 76 =====')
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dado em forma tabular.

# lista = (
#     'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
#     'Mochila', 120.33, 'Canetas', 22.30, 'Livro', 34.90)
#
# print('-' * 40)
# print(f'{'LISTAGEM DE PREÇOS':^40}')
# print('-' * 40)
#
# for cont in range(0, len(lista), 2):
#     print(f'{lista[cont]:.<30}R${lista[cont + 1]:>7.2f}')
# print('-' * 50)

print('\n *** Resposta do Professor esta comentado ***')

listagem = (
    'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
    'Mochila', 120.33, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
