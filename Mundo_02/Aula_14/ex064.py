print('===== DESAFIO 64 =====')
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).

soma = 0
cont = 0
num = 0
while num != 999:
    num = int(input('Digite um valor: '))
    cont += 1
    soma += num
    if num == 999:
        soma -= 999
        cont -= 1

print('A soma dos {} números informado foi de {} .'.format(cont, soma))

print('\n *** Resposta do Professor esta comentado ***')
#
# num = cont = soma = 0
# num = int(input('Digite um número [999 para parar]: '))
# while num != 999:
#     soma += num
#     cont += 1
#     num = int(input('Digite um número [999 para parar]: '))
# print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
