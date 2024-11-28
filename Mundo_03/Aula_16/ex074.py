print('===== DESAFIO 74 =====')
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

# num1 = randint(1, 10)
# num2 = randint(1, 10)
# num3 = randint(1, 10)
# num4 = randint(1, 10)
# num5 = randint(1, 10)
# numeros = (num1, num2, num3, num4, num5)

# print(f'Os valores sorteados foram: {numeros}')
# print(f'O maior valor sorteado foi {max(numeros)}')
# print(f'O menor valor sorteado foi {min(numeros)}')

print('\n *** Resposta do Professor esta comentado ***')

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
