print('===== DESAFIO 86 =====')
# Crie um programa que crie uma matriz 3.3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela com a formatação correta

# matriz = [[], [], []]
# for n in range(0, 3):
#     matriz[0].append(int(input(f'Digite um valor para {0, n + 1} ')))
# for u in range(0, 3):
#     matriz[1].append(int(input(f'Digite um valor para {1, u + 1} ')))
# for y in range(0, 3):
#     matriz[2].append(int(input(f'Digite um valor para {2, y + 1} ')))
# print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]')
# print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]')
# print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]')
# foi feito, porém muito complexo

print('\n *** Resposta do Professor esta comentado ***')
# melhor elaborado
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# esse For é de alimentação é que vai colocar os valores na lista
for l in range(0, 3):  # for em linha
    for c in range(0, 3):  # for em coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
# esse FOR vai ser para mostar a estrutura na tela
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
