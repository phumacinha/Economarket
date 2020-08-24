from dado.Mercado import Mercado
from dado.Produto import Produto
from dado.Marca import Marca
from dado.Item import Item
from grafo.Aresta import Aresta

class Grafo(object):
    """Classe que modela um grafo e possui método para encontrar o é chamado de
    de Floresta de Steiner.

    O grafo é modelado a partir de uma lista de arestas indexadas pelos
    vértices terminais.
    A Floresta de Steiner é assim chamada pois é um conjunto de Árvores de
    Steiner. O grafo possui vértices terminais e de steiner, que gerará
    uma ou mais Árvores de Steiner.
    
    Args:
        steiner (set): Conjunto de vértices de Steiner.
        terminal (set): Conjunto de vértices terminais.
        arestas (dict): Lista de arestas do grafo indexadas pelos vértices
        terminais.

    Attributes:
        steiner (set): Conjunto de vértices de Steiner.
        terminal (set): Conjunto de vértices terminais.
        arestas (dict): Lista de arestas do grafo indexadas pelos vértices
        terminais.
    """

    def __init__(self):
        self.steiner = set()
        self.terminal = set()
        self.arestas = dict()

    def adicionar_aresta(self, aresta:Aresta):
        """Metodo para adicioar aresta ao grafo.

        Args:
            aresta (Aresta): Aresta a ser adicionada.
        """
        self.terminal.add(aresta.produto.id_produto)
        self.steiner.add(aresta.mercado.id_mercado)
        
        if aresta.produto.id_produto in self.arestas.keys():
            self.arestas[aresta.produto.id_produto].append(aresta)
        else:
            self.arestas[aresta.produto.id_produto] = [aresta]

    def get_aresta_menor_valor(self, id_produto:int) -> Aresta:
        """Método que retorna a menor aresta que parte de um vértice de
        produto.

        Args:
            id_produto (int): Número identificador do produto.

        Returns:
            Aresta de menor valor.
        """
        
        # Lista de arestas do vértice.
        arestas_do_produto = self.arestas[id_produto]

        # Criar aresta com o maior peso possível.
        aresta_menor_valor = Aresta(None, None, None, float('inf'))

        # Percorre todas as arestas do produto verificando a de menor valor.
        for aresta in arestas_do_produto:
            if aresta < aresta_menor_valor:
                aresta_menor_valor = aresta

        return aresta_menor_valor

    def calcula_floresta_steiner(self):
        """Cálcula uma floresta de Steiner.

        Cria-se um novo objeto do tipo Grafo para armazenar o resultado.
        O método percorre cada vértice terminal buscando sua aresta de 
        valor. Essa aresta é adicionada aos vértices da aresta do grafo de
        resultado.

        Returns:
            Grafo que representa a Floresta de Steiner.
        """

        floresta_steiner = Grafo()

        for id_produto in self.terminal:
            aresta_menor_valor = self.get_aresta_menor_valor(id_produto)
            floresta_steiner.terminal.add(id_produto)
            floresta_steiner.steiner.add(aresta_menor_valor.mercado.id_mercado)
            floresta_steiner.adicionar_aresta(aresta_menor_valor)
        
        return floresta_steiner