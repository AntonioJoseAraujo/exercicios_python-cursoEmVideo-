print('===== DESAFIO 20 =====')
# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Digite o nome do 1º aluno: '))
n2 = str(input('Digite o nome do 2º aluno: '))
n3 = str(input('Digite o nome do 3º aluno: '))
n4 = str(input('Digite o nome do 4º aluno: '))
lista = [n1, n2, n3, n4]
escolhido = shuffle(lista)
print('A ordem de apresentação será: {}.'.format(lista))

# random.shuffle(nome da lista) embaralha os itens dentro de uma determinada lista
