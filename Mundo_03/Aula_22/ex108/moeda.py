def aumentar(n=0, a=0):
    r = n + (n * (a / 100))
    return r


def diminuir(n=0, d=0):
    r = n - (n * (d / 100))
    return r


def dobro(n=0):
    return n + n


def metade(n=0):
    return n / 2


def moeda(n, moeda="R$"):
    return f'{moeda} {n:>.2f}'.replace('.', ',')
