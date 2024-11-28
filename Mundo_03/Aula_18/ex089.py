print('===== DESAFIO 89 =====')
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

# lista = list()
# dado = list()
# medias = []
# notas = []
#
# while True:
#     nome = str(input('Nome: '))
#     dado.append(nome)
#     nota1 = float(input(f'Nota 1: '))
#     notas.append(nota1)
#     nota2 = float(input(f'Nota 2: '))
#     notas.append(nota2)
#
#     media = (nota1 + nota2) / 2
#     medias.append(media)
#
#     dado.append(notas[:])
#     dado.append(medias[:])
#     lista.append(dado[:])
#     # lista.append(medias[:])
#     # lista.append(notas[:])
#     dado.clear()
#     notas.clear()
#     medias.clear()
#
#     op = str(input('Deseja continuar? [S/N] '))
#     if op in 'Nn':
#         break
#
# print('-' * 30)
# print(f'Lista {lista}')
# print('-=' * 50)
# print(f'{'No. NOME':<10} {'MÉDIA':>20}')
# print('-' * 40)
# for c, l in enumerate(lista):
#     print(f'{c:<3} {l[0]:<21} {l[2]}')
# print('*********')
# # while True:
# #     n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
# #     if n == len(lista):
# #         print(f'Notas de {lista[0]} são {lista[1]} ')
# #     if n == 999:
# #         break
#
# print('-' * 40)
#
# print('FIM DO PROGRAMA!')

print('\n *** Resposta do Professor esta comentado ***')

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print(' <<< VOLTE SEMPRE >>>')
