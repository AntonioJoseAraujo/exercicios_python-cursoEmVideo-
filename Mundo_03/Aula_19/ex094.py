print('===== DESAFIO 94 =====')
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dado de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# a. Quantas pessoas foram cadastradas
# b. A média de idade do grupo
# c. uma lista com todas as mulheres
# d. uma lista com todas as pessoas com idade acima da média.

# pessoas = {}
# lista = [[], []]
# cont = idade = 0
# while True:
#     pessoas['nome'] = str(input('Nome: '))
#     pessoas['sexo'] = str(input('Sexo: [M/F] '))
#     pessoas['idade'] = int(input('Idade: '))
#     lista.append(pessoas.copy())
#     if pessoas['sexo'] in 'Ff':  # pessoas do sexo F
#         lista[0].append(pessoas['nome'])
#     if pessoas['idade'] >= 30:  # pessoas acima da média
#         lista[1].append(pessoas.copy())
#     cont += 1  # contador de pessoas cadastras
#     idade += pessoas['idade']
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# mediaIdade = idade / cont
# print(f'- Total de pessoas cadastradas foi de {cont}.')  # contador
# print(f'- A média de idade é de {mediaIdade:.2f} anos.')
# print(f'- As mulheres cadastradas foram: {lista[0][0]}')
# print(f'- Lista de pessoas que esta acima da idade:')
# for p in lista[1]:
#     print(f'{p};')

print('\n *** Resposta do Professor esta comentado ***')
# MUITO mais detalhado do que foi feito, não está errado oque foi feito.

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apanas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')
