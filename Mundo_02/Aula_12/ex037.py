print('===== DESAFIO 37 =====')
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


num = int(input('Digite um número inteiro: '))
# hexa = hex(num)
# octal = oct(num)
# bina = bin(num)
op = int(input('Qual a forma de conversão que deseja?\n'
               '[1] - Binário\n'
               '[2] - Octal\n'
               '[3] - Hexadecimal\n'
               'Escolha sua opção: '))
if op == 1:
    print('O valor de {} em Binário é {}'.format(num, bin(num[2:])))
elif op == 2:
    print('O valor de {} em Octal é de {}'.format(num, oct(num[2:])))
elif op == 3:
    print('O valor de {} em Hexadecimal é de {}'.format(num, hex(num[2:])))
else:
    print('Opção Invalida!')

print('\n----- Resolução do Professor esta comentada -----')
# Foi exatamente oque foi feito. Somente faltou tirar as letras que aparecem na frente da resposta como no Binário
# aparecia 0b1101001. Foi feito um fatiamento da informação colocando o [2:] para tirar essas informações.
