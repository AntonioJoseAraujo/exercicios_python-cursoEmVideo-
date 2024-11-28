print('===== DESAFIO 63 =====')
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('*** Sequencia Fibonacci ***')
s1 = 0
s2 = 1
cont = 1
n = int(input('Quantos valores sera exibidos: '))
print('{} - '.format(s1), end='')
while cont <= n:
    s1 = s1 + s2
    s2 = s1 - s2
    cont += 1
    print('{}'.format(s1), end=' - ')
print('FIM.')

print('\n*** Resposta do Professor esta comentado ***')
# print('-' * 30)
# print('Sequência de Fibonacci')
# print('-' * 30)
# n = int(input('Quantos termos você quer mostrar? '))
# t1 = 0
# t2 = 1
# print('~' * 30)
# print('{} -> {}'.format(t1, t2), end='')
# cont = 3
# while cont <= n:
#     t3 = t1 + t2
#     print(' -> {}'.format(t3), end='')
#     t1 = t2
#     t2 = t3
#     cont += 1
# print(' => FIM')
# print('~' * 30)
