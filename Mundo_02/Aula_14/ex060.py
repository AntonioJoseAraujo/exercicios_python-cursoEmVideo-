print('===== DESAFIO 60 =====')
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# não consegui fazer, resposta do professor

from math import factorial

# n = int(input('Digite um número para calcular o Fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))

# código a cima está certo, porém não mostra a sequência como no exemplo.

n = int(input('Digite um número para calcular o Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

print('\n*** Usando FOR esta comentado ***')
# Desafio feito pelo professor. (Feito)
# n = int(input('Qual é o valor do Fatorial: '))
# f = 1
# c = n
# print('Calculando {}! = '.format(n), end='')
# for c in range(n, 0, -1):
#     print('{}'.format(c), end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
# print('{}'.format(f))
