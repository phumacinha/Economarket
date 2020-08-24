class Mercado(object):
    """Classe que representa um mercado.
    
    Args:
        id_mercado (int): Número identificador do mercado.
        nome (str): Nome do mercado.

    Attributes:
        id_mercado (int): Número identificador do mercado.
        nome (str): Nome do marca.
    """

    def __init__(self, id_mercado:int, nome:str):
        self.id_mercado = id_mercado
        self.nome = nome
