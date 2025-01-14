# Familia de Produtos do tema Faroeste
class Cavalo:
    def movimentar(self):
        print("Pocotó, Pocotó, Pocotó...")


class Cauboi:
    def falar(self):
        print('Irráaa')


class Revolver:
    def atirar(self):
        print('Pow!')


# Familia de Produtos do tem Espacial
class Nave:
    def movimentar(self):
        print("Vshhhh")


class Piloto:
    def falar(self):
        print('Ativar velocidade de dobra espacial')


class PistolaLaser:
    def atirar(self):
        print('Pew! Pew!')


class Tema:
    """
    Classe Fábrica "abstrata" para criação das Fábricas concretas
    """

    def criar(self, item: str):
        """
        Retorna um novo objeto do tipo item de acordo com o tema escolhido
        """
        return self.itens.get(item)()


class Faroeste(Tema):
    def __init__(self):
        self.itens = {
            'veiculo': Cavalo,
            'personagem': Cauboi,
            'arma': Revolver
        }


class Espaço(Tema):
    def __init__(self):
        self.itens = {
            'veiculo': Nave,
            'personagem': Piloto,
            'arma': PistolaLaser
        }


if __name__ == '__main__':
    # Cria uma lista de todas as Fabricas concretas possíveis
    temas = [t.__name__ for t in Tema.__subclasses__()]
    # Cria um menu para ecolha do Tema
    print('Escolha o tema do jogo:')
    for i, t in enumerate(temas):
        print(f'{i}) {t}')
    tema = int(input('Tema : '))
    # Iniciliza o Jogo com o cenario escolhido
    cenario = Tema.__subclasses__()[tema]()
    veiculo = cenario.criar('veiculo')
    personagem = cenario.criar('personagem')
    arma = cenario.criar('arma')
    # Utiliza os itens de acordo com o cenário escolhido
    arma.atirar()
    personagem.falar()
    veiculo.movimentar()
