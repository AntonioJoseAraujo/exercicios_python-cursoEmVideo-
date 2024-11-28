# def aumentar(n=0, a=0, sit=False):
#     moeda = "R$"
#     r = n + (n * (a / 100))
#     if sit:
#         return f'{moeda} {r:.2f}'.replace('.', ',')
#     else:
#         return f'{r}'.replace('.', ',')
#
#
# def diminuir(n=0, d=0, sit=False):
#     moeda = "R$"
#     r = n - (n * (d / 100))
#     if sit:
#         return f'{moeda} {r:.2f}'.replace('.', ',')
#     else:
#         return f'{r}'.replace('.', ',')
#
#
# def dobro(n=0, sit=False):
#     moeda = "R$"
#     n = n + n
#     if sit:
#         return f'{moeda} {n:.2f}'.replace('.', ',')
#     else:
#         return f'{n}'.replace('.', ',')
#
#
# def metade(n=0, sit=False):
#     moeda = "R$"
#     n = n / 2
#     if sit:
#         return f'{moeda} {n:.2f}'.replace('.', ',')
#     else:
#         return f'{n}'.replace('.', ',')
#
#
# def moeda(n, moeda="R$"):
#     return f'{moeda} {n:.2f}'.replace('.', ',')


# *** Resposta do Professor está comentado ***
# A validação do professor ficou melhor, e mais bem explicada

def aumentar(n=0, a=0, formato=False):
    resp = n + (n * (a / 100))
    return resp if formato is False else moeda(resp)


def diminuir(n=0, d=0, formato=False):
    resp = n - (n * (d / 100))
    return resp if not formato else moeda(resp)


def dobro(n=0, formato=False):
    resp = n + n
    return resp if formato is False else moeda(resp)


def metade(n=0, formato=False):
    resp = n / 2
    return resp if not formato else moeda(resp)


def moeda(n, moeda="R$"):
    return f'{moeda} {n:.2f}'.replace('.', ',')
