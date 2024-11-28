print('===== DESAFIO 62 =====')
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.


primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão:'))
termo = 0
cont = 1
add = 10
print('-' * 30)
print('Os 10 primeiros termos da PA :')

while add != 0:
    termo += add
    while cont <= termo:
        print('{} '.format(primeiro), end=' > ')
        primeiro += razao
        cont += 1
    print('...')
    add = int(input('Deseja ver mais quantos Termos da PA? '))
print('ACABOU.')

print('\n *** Resposta do Professor esta comentado ***')

# print('Gerador de PA')
# print('-=' * 10)
# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão da PA: '))
# termo = primeiro
# cont = 1
# total = 0
# mais = 10
# while mais != 0:
#     total = total + mais
#     while cont <= total:
#         print('{} => '.format(termo), end='')
#         termo += razao
#         cont += 1
#     print('PAUSA')
#     mais = int(input('Quantos termos você quer mostrar a mais? '))
# print('Progressão finalizada com {} termos mostrados.'.format(total))
