print('===== DESAFIO 97 =====')


# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva("Olá, Mundo!")
# Saída:
# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~

def escreva(txt):
    tamanho = len(txt)
    print('~' * tamanho)
    print(txt)
    print('~' * tamanho)


# Programa Principal
escreva('Olá, Mundo!')
escreva('Antônio José de Araújo')
escreva('Aprendendo Python no Curso em Vídeo')

print('\n *** Resposta do Professor esta comentado ***')
'''Unica diferença foi o print no texto que ele formatou colocando espaços para ficar alinhado'''


def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


# Programa Principal
escreva('Olá, Mundo!')
escreva('Antônio José de Araújo')
escreva('Aprendendo Python no Curso em Vídeo')
escreva('CeV')
