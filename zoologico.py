from abc import ABC, abstractmethod #abc é a sigla para Abstract Base Classes (Classes Base Abstratas).

# Classe abstrata para definir o comportamento geral dos animais
class Animal(ABC):
    def __init__(self, nome, especie):
        self._nome = nome  # Atributo encapsulado
        self._especie = especie

    @abstractmethod
    def emitir_som(self):
        """Método abstrato que será implementado pelas subclasses"""
        pass

    def __str__(self):
        return f"{self._nome} ({self._especie})"

# Subclasses de Animal (herança e polimorfismo)
class Leao(Animal):
    def emitir_som(self):
        return "Rugido!"

class Papagaio(Animal):
    def emitir_som(self):
        return "Squawk!"

class Cobra(Animal):
    def emitir_som(self):
        return "Ssssss!"

# Classe Tratador (composição)
class Tratador:
    def __init__(self, nome):
        self.nome = nome
        self.animais = []  # Coleção de objetos Animal

    def adicionar_animal(self, animal):
        """Adiciona um animal aos cuidados do tratador."""
        if isinstance(animal, Animal):  # Verifica se é um objeto da classe Animal ou derivada
            self.animais.append(animal)
            print(f"{animal} foi adicionado aos cuidados de {self.nome}.")
        else:
            print("Apenas objetos do tipo Animal podem ser adicionados.")

    def alimentar_animais(self):
        """Simula o ato de alimentar todos os animais."""
        print(f"{self.nome} está alimentando os animais:")
        for animal in self.animais:
            print(f"- {animal} está comendo feliz!")

    def fazer_animais_emitirem_som(self):
        """Faz todos os animais emitirem seus sons."""
        print(f"{self.nome} está fazendo os animais emitirem seus sons:")
        for animal in self.animais:
            print(f"- {animal}: {animal.emitir_som()}")

# Exemplo de uso
if __name__ == "__main__":
    # Criando objetos Animal
    simba = Leao("Simba", "Leão")
    polly = Papagaio("Polly", "Papagaio")
    kaa = Cobra("Kaa", "Cobra")

    # Criando um Tratador
    tratador = Tratador("João")

    # Adicionando animais aos cuidados do tratador
    tratador.adicionar_animal(simba)
    tratador.adicionar_animal(polly)
    tratador.adicionar_animal(kaa)

    # Exibindo ações
    tratador.alimentar_animais()
    tratador.fazer_animais_emitirem_som()




