print('===== DESAFIO 39 =====')
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Qual é o ano de seu nascimento? '))
idade = date.today().year - ano
sexualidade = int(input('''Você é Homem ou Mulher ?
[1] - Homem
[2] - Mulher
Opção: '''))
if sexualidade == 1:
    if idade < 18:
        print('Ainda não é hora de se alistar.\n'
              'Falta(m) {} ano(s) para o alistamento obrigatório.\n'
              'Seu alistamento será em {}.'.format(18 - idade, ano + 18))
    elif idade == 18:
        print('Já esta na hora de se alistar.')
    else:
        print('Você já deveria ter se alistado há {} ano(s).\n'
              'Seu alistamento foi em {}.'.format(idade - 18, ano + 18))
else:
    print('Mulheres não precisa se alistar.')
print('\n----- Resolução do Professor esta comentada -----')
