from dado.Produto import Produto

from openpyxl import load_workbook
from openpyxl import Workbook
import os
import time
from ListaDeCompra import ListaDeCompra
from dado.Item import Item
from dado.Mercado import Mercado
from dado.Marca import Marca

dados = load_workbook('dados.xlsx')
produtos = [Produto(id_produto+1, produto[0].value) for id_produto, produto in enumerate(dados['produto'])]
produtos_selecionados = set()

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_cabecalho():
    limpar_terminal()

    print('\033[42m'+' '*15+'\033[0;0m')
    print('\033[42m'+'\033[30m'+'\033[1m'+'  ECONOMARKET  '+'\033[0;0m')
    print('\033[42m'+' '*15+'\033[0;0m'+'\n')

def imprimir_menu(titulo:str, opcoes:list):
    imprimir_cabecalho()

    imprimir_lista_selecionada()

    print('\033[1m'+titulo+':'+'\033[0;0m')

    print('-'*32)
    codigo = 1
    for opcao in opcoes:
        print('{:>2} - {:<30}'.format(codigo, opcao))
        codigo += 1
    print('-'*32, '\n')

def menu_principal(texto_input:str='Selecione uma opção'):
    opcoes = ['Adicionar produtos à lista', 'Remover produtos da lista', 'Finalizar e fazer orçamento.']
    imprimir_menu('Opções', opcoes)
    
    entrada = input(texto_input+': ')
    if not entrada.isdigit() or int(entrada) < 1 or int(entrada) > len(opcoes):
        return menu_principal('\033[1m\033[31mOpção inválida!\033[0;0m\nSelecione uma opção válida')
    
    entrada = int(entrada)
    if entrada == 1:
        return adicionar_produtos()
    elif entrada == 2:
        return remover_produtos()
    elif entrada == 3:
        return gerar_lista()

def imprimir_lista_selecionada():
    global produtos, produtos_selecionados

    lista = [produtos[codigo_produto-1].nome for codigo_produto in produtos_selecionados]

    if len(produtos_selecionados):
        print('Sua lista:', end=' ')
        print(', '.join(lista))
    else:
        print('Sua lista está vazia.')
    
    print()

def adicionar_produtos(texto_input:str='Selecione um produto pelo código (digite 0 para voltar ao menu principal)'):
    global produtos
    opcoes = [produto.nome for produto in produtos]
    imprimir_menu('Menu de produtos', opcoes)

    codigo_produto = input(texto_input+': ')
    if not codigo_produto.isdigit() or int(codigo_produto) < 0 or int(codigo_produto) > len(opcoes):
        return adicionar_produtos('\033[1m\033[31mOpção inválida!\033[0;0m\nSelecione um produto pelo código (digite 0 para voltar ao menu principal')
    
    codigo_produto = int(codigo_produto)

    if codigo_produto == 0:
        return menu_principal()
    
    produtos_selecionados.add(codigo_produto)
    return adicionar_produtos()

def remover_produtos(texto_input:str='Digite o código do produto a ser removido (digite 0 para voltar ao menu principal)'):
    global produtos, produtos_selecionados

    if len(produtos_selecionados):
        opcoes = [produtos[codigo_produto-1].nome for codigo_produto in produtos_selecionados]
        imprimir_menu('Produtos na sua lista', opcoes)

        codigo_produto = input(texto_input+': ')
        if not codigo_produto.isdigit() or int(codigo_produto) < 0 or int(codigo_produto) > len(opcoes):
            return adicionar_produtos('\033[1m\033[31mOpção inválida!\033[0;0m\nDigite o código do produto a ser removido (digite 0 para voltar ao menu principal')

        codigo_produto = int(codigo_produto)

        if codigo_produto != 0:
            lista_aux = list(produtos_selecionados)
            lista_aux.pop(codigo_produto-1)
            produtos_selecionados = set(lista_aux)
        
        if codigo_produto == 0 or len(produtos_selecionados) == 0:
            return menu_principal()
        
        return remover_produtos()

    else:
        print('\033[1m\033[31mSua lista está vazia!\033[0;0m')
        time.sleep(1)
        return menu_principal()

def gerar_lista():
    global dados, produtos_selecionados

    if len(produtos_selecionados):
        imprimir_cabecalho()
        print('\033[1mAguarde, estamos gerando sua lista...\033[0;0m')
        lista_de_compra = ListaDeCompra([produtos[codigo_produto-1] for codigo_produto in produtos_selecionados])

        mercados = [mercado[0].value for mercado in dados['mercado']]
        marcas = [marca[0].value for marca in dados['marca'] if marca[0].value is not None]
        for item in dados['item']:
            if item[0].value is None or int(item[1].value) not in produtos_selecionados:
                continue

            id_mercado = int(item[0].value)
            mercado = Mercado(id_mercado, mercados[id_mercado-1])
            
            id_produto = int(item[1].value)
            produto = produtos[id_produto-1]

            id_marca = int(item[2].value)
            marca = Marca(id_marca, marcas[id_marca-1])

            valor = float(item[3].value)
            lista_de_compra.adicionar_item(Item(mercado, produto, marca, valor))

        lista_de_compra.gerar_lista()
        imprimir_cabecalho()
        print('Sua lista está pronta. Agora você pode economizar!')
        
        for lista_mercado in lista_de_compra.lista.values():
            print('\033[47m\033[30m\033[1mLista do mercado '+lista_mercado.mercado.nome+'\033[0;0m')
            print('-'*65)
            print('\033[1m{:<30} | {:<20} | {:<9}\033[0;0m'.format('PRODUTO', 'MARCA', 'VALOR'))
            print('-'*65)
            for item in lista_mercado.itens:
                print('{:<30} | {:<20} | R$ {:>6}'.format(item.produto.nome, item.marca.nome, '%.2f'%item.valor))
                print('-'*65)
            print()
        
    else:
        print('\033[1m\033[31mSua lista está vazia!\033[0;0m')
        time.sleep(1)
        return menu_principal()

def main():
    imprimir_lista_selecionada()
    menu_principal()




    

if __name__ == "__main__":
    main()