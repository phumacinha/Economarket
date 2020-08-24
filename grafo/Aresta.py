from dado.Produto import Produto
from dado.Mercado import Mercado
from dado.Marca import Marca

class Aresta(object):
    """Classe que representa a aresta do grafo.
    
    Nesse modelo de aresta, cada um de seus dois vértices são representados,
    respectivamente, por um mercado e um produto. Além disso, essa classe
    armazena a marca do produto e seu valor.

    Args:
        mercado (Mercado): Mercado que representa um vértice da aresta.
        produto (Produto): Produto que representa o outro vértice da aresta.
        marca (Marca): Marca do produto.
        valor (float): Peso da aresta definido pelo valor do produto.

    Attributes:
        mercado (Mercado): Mercado que representa um vértice da aresta.
        produto (Produto): Produto que representa o outro da aresta.
        marca (Marca): Marca do produto.
        valor (float): Peso da aresta definido pelo valor do produto.
    """

    def __init__(self, mercado:Mercado, produto:Produto, marca:Marca, valor:float):
        self.mercado = mercado
        self.produto = produto
        self.marca = marca
        self.valor = valor


    def __lt__(self, outra_aresta) -> bool:
        """Sobrecarga do operador "menor que" para verificar qual aresta possui
        menor valor.

        Args:
            outra_aresta (Aresta): Aresta que deseja-se compara o valor.

        Returns:
            True se essa aresta possui menor valor, False caso contrário.

        """
        return self.valor < outra_aresta.valor