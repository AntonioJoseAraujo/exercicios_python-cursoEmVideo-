print('===== DESAFIO 57 =====')
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

# tive problemas com as condições do while, pois ficou repetindo infinitamente porque coloquei de uma forma que não
# parava.
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[
    0]  # o upper com o 0 vai pegar somente a primeira letra digitada
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

print('\n*** Outra forma de ter feito mais completa esta comentado ***')

# genero = str(input('Informe o seu gênero [M / F]? ')).strip().upper()
#
# while genero != 'M' and genero != 'F':
#     print('=-' * 20)
#     genero = str(input('Opção Inválida. Informe o seu gênero [M / F]? ')).strip().upper()
#
# print('=-' * 20)
# if genero == 'M':
#     print('Gênero MASCULINO registrado com sucesso!')
# else:
#     print('Gênero FEMININO registrado com sucesso!')
