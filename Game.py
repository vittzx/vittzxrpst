# vittzxrpst
Vittzx's Projects

from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input("Qual o nivel de dificuldade desejada [1, 2, 3 ou 4]"))
    calc : Calcular = Calcular(dificuldade)

    print("Informe seu resulta:")
    calc.mostra_operacao()
    resultado = int(input())

    if calc.checar_resultados(resultado): # se for True
        pontos += 1
        print(f'Voce tem {pontos} pontos!')

    continuar: int = int(input('Quer continuar? 1-sim, 0-Nao'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Voce finalizou com {pontos} pontos!')
        print(f'Até a proxima ')





if __name__ == '__main__':
    main()











