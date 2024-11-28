print('===== DESAFIO 16 =====')
# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
# Inteira.

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, int(num)))


'''OUTRAS ALTERNATIVAS DE RESOLUÇÃO:
Importando múdulos:
a função math.trunc() separa a parte inteira de um número;
a função math.floor() arredonda o número para baixo;'''
