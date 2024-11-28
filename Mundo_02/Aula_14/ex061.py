print('===== DESAFIO 61 =====')
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
cont = 1
while cont <= 10:
    primeiro += razao
    print('{} '.format(primeiro), end=' > ')
    cont += 1

print('ACABOU')

print('\n *** Resposta do Professor esta comentado ***')

# print('Gerador de PA')
# print('-=' * 10)
# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão da PA: '))
# termo = primeiro
# cont = 1
# while cont <= 10:
#     print('{} => '.format(termo), end='')
#     termo += razao
#     cont += 1
# print('FIM')
