print('===== DESAFIO 59 =====')
# Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior,
# [ 4 ] novos números, [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
op = 0
while op != 5:
    op = int(input('''Qual opção você deseja realizar com os valores informados.
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    Opção:'''))
    print('-' * 50)
    if op == 1:
        soma = n1 + n2
        print('A Soma de {} + {} é igual a {}.'.format(n1, n2, soma))
        print('-' * 50)
    elif op == 2:
        mult = n1 * n2
        print('A Multiplicação dos valores {} e {} é de {}.'.format(n1, n2, mult))
        print('-' * 50)
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número informado foi {}.'.format(maior))
        print('-' * 50)
    elif op == 4:
        op = 0
    else:
        print('Opção Inválida! Tente Novamente.')
    print('*-*' * 10)
print('*** Fim do programa! ***')
print('\n --- Resposta do Professor esta comentado ---')

# from time import sleep
#
# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))
# opcao = 0
# while opcao != 5:
#     print('''    [1] Somar
#     [2] Multiplicar
#     [3] Maior
#     [4] Novos números
#     [5] Sair do programa''')
#     opcao = int(input('Qual é sua opção? '))
#     if opcao == 1:
#         soma = n1 + n2
#         print('A soma entre {} + {} é {}'.format(n1, n2, soma))
#     elif opcao == 2:
#         mult = n1 * n2
#         print('O resultado de {} x {} é {}'.format(n1, n2, mult))
#     elif opcao == 3:
#         if n1 > n2:
#             maior = n1
#         else:
#             maior = n2
#         print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
#     elif opcao == 4:
#         print('Informe os números novamente:')
#         n1 = int(input('Primeiro valor: '))
#         n2 = int(input('Segundo valor: '))
#     elif opcao == 5:
#         print('Finalizando...')
#     else:
#         print('Opção inválida. Tente novamente.')
#     print('=-=' * 10)
#     sleep(2)
# print('Fim do programa! Volte sempre!')
