print('===== DESAFIO 53 =====')
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# Tem duas formas de ser feito com o FOR e sem
'''inverso = ''
for letra in range(len(junto) -1, -1 -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')
