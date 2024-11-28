print('===== DESAFIO 80 =====')
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# verifiquei outras respostas para fazer
lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:  # o primeiro valor para o fim da lista
        print('Valor foi para o final da lista.')
        lista.append(num)
    else:  # aqui os valores vão para o começo da lista
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'O valor {num} foi adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores adicionados em ordem forram {lista}')

print('\n *** Resposta do Professor esta comentado ***')

# lista = []
# for c in range(0, 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n > lista[-1]: # se for o primeiro valor ele vai add na lista, ou n foi maior que o último valor da lista
#        lista.append(n)
#        print('Adicionado ao final da lista...')
#     elif n > lista[-1]:# não precisa desse elif, pois foi colocado no if acima
#         lista.append(n)
#     else:
#        pos = 0
#        while pos < len(lista):
#            if n <= lista[pos]:
#                lista.insert(pos, n)
#                print(f'Adicionado na posição {pos} da lista...')
#                break
#             pos += 1
#
# print('-=' * 30)
# print(f'Os valores digitados em ordem foram {lista}')
