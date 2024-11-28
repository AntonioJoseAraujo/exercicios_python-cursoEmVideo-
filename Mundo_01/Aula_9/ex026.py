print('===== DESAFIO 26 =====')
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase: ')
print('Quantidades de A na frase é:', frase.count('A', 0))
print('Onde esta a letra A aparece primeiro em sua frase:', frase.find('A'))


# -----------------------------------------------------------
frase = str(input('Digite uma frase: ')).strip().upper()

qtdA = frase.count('A')
pA = frase.find('A') + 1   # mudar o início da contagem de 0 para 1
uA = frase.rfind('A') + 1

print('Analisando a frase...\n'
      'Quantas letras A aparecem? {};\n'
      'A 1a letra A aparece na posicão {};\n'
      'A última letra A aparece na posição {}.'.format(qtdA, pA, uA))