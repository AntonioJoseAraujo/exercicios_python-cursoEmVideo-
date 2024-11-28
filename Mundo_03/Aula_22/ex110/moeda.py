def aumentar(n=0, a=0, sit=True):
    moeda = "R$"
    r = n + (n * (a / 100))
    if sit:
        return f'{moeda} {r:.2f}'.replace('.', ',')
    else:
        return f'{r}'.replace('.', ',')


def diminuir(n=0, d=0, sit=True):
    moeda = "R$"
    r = n - (n * (d / 100))
    if sit:
        return f'{moeda} {r:.2f}'.replace('.', ',')
    else:
        return f'{r}'.replace('.', ',')


def dobro(n=0, sit=True):
    moeda = "R$"
    n = n + n
    if sit:
        return f'{moeda} {n:.2f}'.replace('.', ',')
    else:
        return f'{n}'.replace('.', ',')


def metade(n=0, sit=True):
    moeda = "R$"
    n = n / 2
    if sit:
        return f'{moeda} {n:.2f}'.replace('.', ',')
    else:
        return f'{n}'.replace('.', ',')


def moeda(n, moeda="R$"):
    return f'{moeda} {n:.2f}'.replace('.', ',')


# a = aumento
# d = dimimui
# n = valor
# def resumo(n, a, d):
#     print('-' * 50)
#     print(f'{'RESUMO DO VALOR':^50}')
#     print('-' * 50)
#     print(f'{'Preço analisado:':<30}{moeda(n)}')
#     print(f'{'Dobro do preço:':<30}{dobro(n)}')
#     print(f'{'Metade do preço:':<30}{metade(n)}')
#     print(f'{a}{'% de aumento:':<28}{aumentar(n, a)}')
#     print(f'{d}{'% de redução:':<28}{diminuir(n, d)}')
#     print('-' * 50)

# RESPOSTA FEITA PELO PROFESSOR
def resumo(preço=0, taxaa=10,
           taxar=5):  # Esses valores nas taxas são os padrões, se não colocar as taxas no programa principal
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(50))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço)}')
    print(f'Metade do preço: \t{metade(preço)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar)}')
    print('-' * 30)
