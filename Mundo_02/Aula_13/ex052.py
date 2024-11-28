print('===== DESAFIO 52 =====')
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# for c in range(1, 5):
#     num = int(input('Digite um número inteiro: '))
#
#     if num % 2 == 0 or num % 3 == 0:
#         print('O número {} NÃO é primo.'.format(num))
#     else:
#         print('O número {} é primo.'.format(num))
# print('FIM')

print('*** Resposta do Professor ***')
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vez'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO.')
else:
    print('E por isso ele NÃO É PRIMO.')
