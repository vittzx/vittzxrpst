from utils.helper import formata_float_str

class Produto:
    contador : int = 1

    def __init__(self: object, nome: str, preco: float ) -> None:
        self.__codigo = Produto.contador
        self.__nome = nome
        self.__preco = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float :
        return self.__preco

    def __str__(self: object) -> str:
        return f'Codigo: {self.codigo} \nNome:{self.nome} \nPreco:{formata_float_str(self.preco)}'
