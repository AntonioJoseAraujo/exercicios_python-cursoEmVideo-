def linha(tam=50):
    return '-' * tam


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um número inteiro válido!\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def cabecalho(txt):
    print(f'\033[34m{linha()}\033[3m')
    print(f'\033[34m{txt.center(50)}\033[m')
    print(f'\033[34m{linha()}\033[m')


def menu(lista):
    cabecalho('Sistema MENU CHAVEIRO')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    opc = leiaInt(f'\033[32mSua opção: \033[m')
    return opc
