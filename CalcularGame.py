import random

class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: float = self._gerar_valor
        self.__valor2: float = self._gerar_valor
        self.__operacao: int = random.randint(1, 3)
        self.__resultado: float = self._gerar_resultado

    @property
    def dificuldade(self: object ) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> float:
        return self.__valor1

    @property
    def valor2(self: object) -> float:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> float :
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.__operacao == 1:
            op: str = 'Somar'

        elif self.__operacao == 2:
            op: str = 'Subtrair'

        elif self.__operacao == 3:
            op: str = 'Multiplicar'

        else:
            op: str = 'Operacao desconhecida'

        return f'Valor1:{self.valor1}\nValor2:{self.valor2}\n' \
               f'Operação:{op}\nDificuldade:{self.dificuldade} '

    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return random.randint(1, 10)

        elif self.dificuldade == 2:
            return random.randint(1, 100)

        elif self.dificuldade == 3:
            return random.randint(1, 1000)

        elif self.dificuldade == 4:
            return random.randint(1, 10000)

        else:
            return random.randint(1, 100000)



    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2

        elif self.operacao == 2:
            return self.valor1 - self.valor2

        else:
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'


    def checar_resultados(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            certo = True
            print('Resposta correta!')
        else:
            print('Errou animal, burro do caralho!')
        print(f'A resposta certa é {self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo


    def mostra_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} =? ')
