print('===== DESAFIO 40 =====')
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média foi de {}\n'
          'Você foi Reprovado!'.format(media))
elif media == 5.0 or media <= 6.9:
    print('Sua média foi de {}\n'
          'Você esta de Recuperação!'.format(media))
elif media >= 7.0:
    print('Sua média foi de {}\n'
          'Você esta Aprovado!'.format(media))

print('\n----- Resolução do Professor esta comentada -----')

# nota1 = float(input('Primeira nota: '))
# nota2 = float(input('Segunda nota: '))
# media = (nota1 + nota2) / 2
# print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1}'.format(nota1, nota2, media))
# if 7 > media >= 5:
#     print('O aluno está em RECUPERAÇÃO.')
# elif media < 5:
#     print('O aluno está REPROVADO.')
# elif media >= 7:
#     print('O aluno esta APROVADO.')
