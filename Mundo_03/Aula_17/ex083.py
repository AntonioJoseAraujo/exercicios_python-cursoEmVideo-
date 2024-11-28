print('===== DESAFIO 83 =====')
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.EXEMPLO:
# ((a+b) * 2) CORRETO
# ((a+b) * (a*c) +2 ERRADO
# Fazer isso com lista
# NÃO CONSEGUI FAZER DE NEM UMA FORMA

print('\n *** Resposta do Professor esta comentado ***')

expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:  # para cada símbolo em expressão
    if símb == '(':  # verifica para adicionar
        pilha.append('(')  # adicionar na lista
    elif símb == ')':
        if len(pilha) > 0:  # verifica se tem elemento na lista
            pilha.pop()  # vai remover um elemento da lista
        else:  # se a pilha estiver vazia
            pilha.append(')')
            break
# vai add e depois remover
if len(pilha) == 0:  # se a lista for 0
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
