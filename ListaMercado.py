from dado.Mercado import Mercado
from dado.Item import Item

class ListaMercado(object):
    def __init__(self, mercado:Mercado):
        self.mercado = mercado
        self.itens = []
        self.valor_total = 0

    def adicionar_item(self, item:Item):
        self.itens.append(item)
        self.valor_total += item.valor

    def imprimir(self):
        mercado = self.mercado.nome
        print('-'*30)
        print('{}:'.format(mercado))
        print('-'*30)

        for item in self.itens:
            print('Produto: {} | Marca: {} | Valor: {:.2f}'.format(item.produto.nome, item.marca.nome, item.valor))
        
        print('\Valor: R$ {:.2f}'.format(self.valor_total))
