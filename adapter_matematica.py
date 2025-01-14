import math as m


class Matematica:
    """
    Classe que adapta os métodos do módulo math do python
    """
    @staticmethod
    def logaritmoe(x):
        return m.log(x)

    @staticmethod
    def logaritmo2(x):
        return m.log2(x)

    @staticmethod
    def logaritmo(x, base):
        return m.log(x, base)


if __name__ == '__main__':
    # Testa a execução do adaptador
    mat = Matematica()
    print(f'O logaritmo na base natural de 2 é: {mat.logaritmoe(2)}')
    print(f'O logaritmo na base 2 de 32 é: {mat.logaritmo2(32)}')
