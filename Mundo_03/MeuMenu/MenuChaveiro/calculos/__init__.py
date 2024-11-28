from Mundo_03.MeuMenu.MenuChaveiro import *
from time import sleep


def saidaProd(arq_prod, tipo='desconhecido', modelo='desconhecido', qtd_saida=0):
    try:
        # Abre o arquivo para leitura e escrita
        with open(arq_prod, 'r+') as a:
            linhas = a.readlines()

        # Remove espaços extras e converte a primeira letra de cada palavra para maiúscula
        tipo = tipo.strip().title()
        modelo = modelo.strip().title()

        produto_encontrado = False  # Flag para indicar se o produto foi encontrado

        # Adiciona mensagem de depuração para indicar que a verificação começou
        print('Verificando produtos...')
        sleep(3)

        # Percorre as linhas do arquivo em blocos de 3 (tipo, modelo, quantidade)
        for i in range(0, len(linhas), 3):
            # Remove espaços extras e ponto e vírgula, e converte a primeira letra de cada palavra para maiúscula
            tipo_linha = linhas[i].strip().replace(';', '').title()
            modelo_linha = linhas[i + 1].strip().replace(';', '').title()

            # Verifica se o tipo e modelo correspondem aos fornecidos pelo usuário
            if tipo_linha == tipo and modelo_linha == modelo:
                # Remove o ponto e vírgula e converte a quantidade para inteiro
                qtd_linha = int(linhas[i + 2].strip().replace(';', ''))
                print(f'Produto encontrado: Tipo: {tipo_linha}, Modelo: {modelo_linha}, Quantidade: {qtd_linha}')

                # Verifica se a quantidade a ser subtraída é maior do que a disponível
                if qtd_saida > qtd_linha:
                    print(
                        f'\033[31mErro: Quantidade de saída ({qtd_saida}) maior do que a quantidade disponível ({qtd_linha}).\033[m')
                    return False

                # Subtrai a quantidade e atualiza a linha
                nova_qtd = qtd_linha - qtd_saida
                linhas[i + 2] = str(nova_qtd) + ';\n'  # Adiciona o ponto e vírgula novamente à quantidade

                produto_encontrado = True  # Define a flag como True

                # Reescreve o arquivo com as alterações
                with open(arq_prod, 'w') as a:
                    a.writelines(linhas)

                print(f'\033[32mSaída de {qtd_saida} unidades do produto {tipo} {modelo} realizada com sucesso!\033[m')
                break  # Sai do loop após encontrar o produto

        # Se o produto não foi encontrado, exibe uma mensagem de erro
        if not produto_encontrado:
            print(f'\033[31mProduto {tipo} {modelo} não encontrado no arquivo.\033[m')

        return produto_encontrado

    except Exception as e:
        # Captura e exibe qualquer exceção que ocorra
        print(f'\033[31mHouve um ERRO: {e}\033[m')
        return False


def entradaProd(arq_prod, tipo='desconhecido', modelo='desconhecido', qtd_entrada=0):
    try:
        with open(arq_prod, 'r+') as a:
            linhas = a.readlines()

        tipo = tipo.strip().title()
        modelo = modelo.strip().title()

        produto_encontrado = False

        print('Verificando produtos...')
        sleep(3)

        for i in range(0, len(linhas), 3):
            tipo_linha = linhas[i].strip().replace(';', '').title()
            modelo_linha = linhas[i + 1].strip().replace(';', '').title()

            if tipo_linha == tipo and modelo_linha == modelo:
                qtd_linha = int(linhas[i + 2].strip().replace(';', ''))
                print(f'Produto encontrado: Tipo: {tipo_linha}, Modelo: {modelo_linha}, Quantidade: {qtd_linha}')

                nova_qtd = qtd_linha + qtd_entrada
                linhas[i + 2] = str(nova_qtd) + ';\n'

                produto_encontrado = True

                with open(arq_prod, 'w') as a:
                    a.writelines(linhas)

                print(
                    f'\033[32mAdicionado {qtd_entrada} unidades do produto {tipo}, {modelo}, realizada com '
                    f'sucesso!\033[m')
                break

        if not produto_encontrado:
            print(f'\033[31mProduto {tipo}, {modelo} não encontrado no arquivo.\033[m')

        return produto_encontrado

    except Exception as e:
        print(f'\033[31mHouve um ERRO: {e}\033[m')
        return False
