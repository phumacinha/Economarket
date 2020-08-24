class Produto(object):
    """Classe que representa um produto.
    
    Args:
        id_produto (int): Número identificador do produto.
        nome (str): Nome do produto.

    Attributes:
        id_produto (int): Número identificador do produto.
        nome (str): Nome do marca.
    """

    def __init__(self, id_produto:int, nome:str):
        self.id_produto = id_produto
        self.nome = nome
