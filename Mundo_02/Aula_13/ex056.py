print('===== DESAFIO 56 =====')
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


# soma_idade = 0
# qtd = 0
# maior = 0
# velho = ''
# for c in range(0, 4):
#     nome = str(input('Qual o nome da pessoa: '))
#     idade = int(input('Qual a idade da pessoa: '))
#     sexo = int(input('''Qual o é o sexo da pessoa:
#      [1] Homem
#      [2] Mulher
#      Opção: '''))
#
#     soma_idade += idade
#
#     if sexo == 2:
#         if idade < 20:
#             qtd += 1
#
#     elif sexo == 1:
#         if idade > maior:
#             maior = idade
#             velho = nome
#
# media = soma_idade / 4
#
# print('''Média de idade {}.
# O nome do Homem mais velho é {}.
# Quantidade de Mulheres com menos de 20 anos é de {}.'''.format(media, velho, qtd))
print('\n *** Resposta do Professor ***')

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
