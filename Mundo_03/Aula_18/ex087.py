print('===== DESAFIO 87 =====')
# Aprimore o desafio anterior, mostrando no final:
# a: a soma de todos os valores pares digitados
# b: a soma dos valores da terceira coluna
# c: o maior valor da segunda linha

# matriz = [[], [], []]
# soma = 0
# for n in range(0, 3):
#     matriz[0].append(int(input(f'Digite um valor para {0, n + 1} ')))
# if matriz[0][0] % 2 == 0:
#     soma += matriz[0][0]
# if matriz[0][1] % 2 == 0:
#     soma += matriz[0][1]
# if matriz[0][2] % 2 == 0:
#     soma += matriz[0][2]
#
# for u in range(0, 3):
#     matriz[1].append(int(input(f'Digite um valor para {1, u + 1} ')))
# if matriz[1][0] % 2 == 0:
#     soma += matriz[1][0]
# if matriz[1][1] % 2 == 0:
#     soma += matriz[1][1]
# if matriz[1][2] % 2 == 0:
#     soma += matriz[1][2]
#
# for y in range(0, 3):
#     matriz[2].append(int(input(f'Digite um valor para {2, y + 1} ')))
# if matriz[2][0] % 2 == 0:
#     soma += matriz[2][0]
# if matriz[2][1] % 2 == 0:
#     soma += matriz[2][1]
# if matriz[2][2] % 2 == 0:
#     soma += matriz[2][2]
#
# print('-=' * 30)
# print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
# print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
# print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')
# print('-=' * 30)
#
# somaTer = matriz[0][2] + matriz[1][2] + matriz[2][2]
# print(f'Soma de todos o valores pares é {soma}')
# print(f'Soma da 3ª coluna é {somaTer}')
# print(f'O maior valor da 2ª linha é {max(matriz[1])}')

print('\n *** Resposta do Professor esta comentado ***')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maior = somaCol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somaPar}.')
for l in range(0, 3):
    somaCol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somaCol}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')
