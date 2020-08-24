class Marca(object):
    """Classe que representa a marca de um produto.
    
    Args:
        id_marca (int): Número identificador da marca.
        nome (str): Nome da marca.

    Attributes:
        id_marca (int): Número identificador da marca.
        nome (str): Nome da marca.
    """

    def __init__(self, id_marca:int, nome:str):
        self.id_marca = id_marca
        self.nome = nome