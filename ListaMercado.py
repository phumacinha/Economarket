from dado.Mercado import Mercado
from dado.Item import Item

class ListaMercado(object):
    """Classe que armazena uma lista de compras por mercado.

    Args:
        mercado (Mercado): Mercado referente à lista de compras.

    Attributes:
        mercado (Mercado): Mercado referente à lista de compras.
        itens (list): Lista de itens da lista de compras.
        valor_total (float): Valor total dos itens desse mercado.
    """
    def __init__(self, mercado:Mercado):
        self.mercado = mercado
        self.itens = []
        self.valor_total = 0

    def adicionar_item(self, item:Item):
        self.itens.append(item)
        self.valor_total += item.valor
