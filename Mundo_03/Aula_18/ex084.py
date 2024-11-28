print('===== DESAFIO 84 =====')
# Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista. No final, mostre:
# a: quantas pessoas foram cadastradas.
# b: uma listagem com as pessoas mais pesadas
# c: uma listagem com as pessoas mais leves
# Obs.: Gerar uma lista com os mais leves e mais pesados vai depender de analisar qual é o mais leve e o mais pesado. Se houver mais de um com esse peso, insere na lista. O mais normal é que a lista de mais pesados tenha apenas 1 pessoa, que é o motivo pelo qual a lista existe.

# pessoas = []
# dado = []
# pesoMaior = []
# pesoMenor = []
#
# totalPessoas = maior = menor = 0
# while True:
#     dado.append(str(input('Nome: ')))
#     dado.append(float(input('Peso: ')))
#     pessoas.append(dado[:])
#
#     if dado[1] >= 100:
#         pesoMaior.append(dado[0])
#         if dado[1] > maior:
#             maior = dado[1]
#
#     if dado[1] <= 80:
#         pesoMenor.append(dado[0])
#         if menor < dado[1] and dado[1] > menor:
#             menor = dado[1]
#         if dado[1] < menor:
#             menor = dado[1]
#     # não to conseguindo validar o menor peso
#     dado.clear()
#     totalPessoas += 1
#
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
#
# print(pessoas)
# print(f'Total de pessoas cadastradas foi de {totalPessoas}')
#
# print(f'O maior peso foi de {maior} Kg. Peso de {pesoMaior}')
# print(f'O menor peso foi de {menor} Kg. Peso de {pesoMenor}')

print('\n *** Resposta do Professor esta comentado ***')

dadosTemp = []
dadosPrinc = []
maior = menor = 0
while True:
    dadosTemp.append(str(input('Nome: ')))
    dadosTemp.append(float(input('Peso: ')))

    if len(dadosPrinc) == 0:
        maior = menor = dadosTemp[1]
    else:
        if dadosTemp[1] > maior:
            maior = dadosTemp[1]
        if dadosTemp[1] < menor:
            menor = dadosTemp[1]

    dadosPrinc.append(dadosTemp[:])
    dadosTemp.clear()

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
# print(f'Os dado foram {dadosPrinc}') #Não foi pedido no exerc porém foi feito para verificar se esta funcionando
print(f'Ao todo, você cadastrou {len(dadosPrinc)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in dadosPrinc:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in dadosPrinc:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
