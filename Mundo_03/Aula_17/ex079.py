print('===== DESAFIO 79 =====')
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:  # se o número não estiver em lista
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:  # se o número estiver na lista
        print('Valor duplicado! Não vou adicionar...')
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Você digitou os valores {sorted(lista)}')

print('\n *** Resposta do Professor esta comentado ***')

# números = list()
# while True:
#     n = int(input('Digite um valor: '))
#     if n not in números:
#         números.append(n)
#         print('Valor adicionado com sucesso...')
#     else:
#         print('Valor duplicado! Não vou adcionar...')
#     r = str(input('Quer continuar? [S/N] '))
#     if r in 'Nn':
#         break
# print('-=' * 30)
# números.sort()
# print(f'Você digitou os valores {números}')
