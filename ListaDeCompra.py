from dado.Item import Item
from grafo.Grafo import Grafo
from ListaMercado import ListaMercado
from grafo.Aresta import Aresta

class ListaDeCompra(object):
    """Classe que armazena calcula e armazena a lista de compra de todos os
    mercados.

    Args:
        produtos (list): Lista de produtos desejados.

    Attributes:
        lista (dict): Dicionário que armazena a lista de compras de cada
        mercado.
        valor_total (float): Valor total dos itens desse orçamento.
        grafo (Grafo): Grafo que será modelado para orçar as compras.
        produtos_indisponiveis (dict): Dicionário que armazena os produtos
        indisponíveis nos mercados.
    """
    def __init__(self, produtos:list):
        self.lista = {}
        self.valor_total = 0
        self.grafo = Grafo()

        self.produtos_indisponiveis = {}
        for produto in produtos:
            self.produtos_indisponiveis[produto.id_produto] = produto

    def adicionar_item(self, item:Item):
        """Adiciona um item como uma aresta no grafo e remove o produto da
        lista de indisponíveis.

        Args:
            item (Item): Item encontrado no banco de dados.
        """
        self.grafo.adicionar_aresta(Aresta(item.mercado, item.produto, item.marca, item.valor))
        if item.produto.id_produto in self.produtos_indisponiveis.keys():
            del self.produtos_indisponiveis[item.produto.id_produto]

    def gerar_lista(self):
        """Calcula a Floresta de Steiner como representação do orçamento.

        Após calcular a Floresta, são extraídas as informações do grafo e
        armezanadas em outras estruturas.
        """
        arvore = self.grafo.calcula_floresta_steiner()

        for aresta in arvore.arestas.values():
            item = Item(aresta[0].mercado, aresta[0].produto, aresta[0].marca, aresta[0].valor)
            self.valor_total = item.valor
            
            if item.mercado.id_mercado not in self.lista.keys():
                self.lista[item.mercado.id_mercado] = ListaMercado(item.mercado)

            self.lista[item.mercado.id_mercado].adicionar_item(item)
