# Programação Orientada a Objetos (POO)

A **Programação Orientada a Objetos (POO)** é um paradigma de programação que organiza o código em torno de "objetos", que representam entidades do mundo real. Esses objetos são instâncias de classes, que funcionam como modelos ou moldes que definem propriedades (atributos) e comportamentos (métodos) que o objeto pode ter. 

Aqui estão os principais conceitos da POO explicados:

## 1. Classes e Objetos
- **Classe**: É a definição ou blueprint de um objeto. Ela descreve quais atributos (dados) e métodos (funções) os objetos criados a partir dela terão.
- **Objeto**: É uma instância de uma classe. Cada objeto possui os atributos definidos pela classe e comporta-se de acordo com os métodos da classe.

## 2. Encapsulamento
O encapsulamento é o princípio de esconder detalhes internos de um objeto, expondo apenas o que é necessário. Ele protege dados sensíveis, permitindo o acesso a atributos e métodos apenas através de interfaces controladas (como getters e setters). Em POO, atributos privados geralmente são usados para implementar o encapsulamento.

``` python

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Atributo privado

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}"
        return "Invalid amount"

    def get_balance(self):
        return self.__balance

# Teste do encapsulamento
account = BankAccount(1000)
print(account.deposit(500))
print("Balance:", account.get_balance())
# print(account.__balance)  # Erro: atributo é privado


```

## 3. Herança
A herança é o mecanismo que permite que uma classe (subclasse) reutilize os atributos e métodos de outra classe (superclasse). Isso promove a reutilização de código e a extensão de funcionalidades, permitindo que subclasses implementem novos comportamentos ou sobrescrevam os existentes.

``` python

class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
print(duck.fly())
print(duck.swim())


```

## 4. Polimorfismo
O polimorfismo é a capacidade de um método, função ou operador se comportar de maneira diferente dependendo do tipo de objeto com o qual está sendo usado. Ele permite a criação de código mais genérico e flexível, em que métodos com o mesmo nome podem ter implementações diferentes dependendo da classe do objeto.

``` python

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Polimorfismo em ação
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())


```

## 5. Classes Abstratas
Uma classe abstrata é uma classe que serve como modelo para outras classes e não pode ser instanciada diretamente. Ela geralmente contém métodos abstratos, que são definidos, mas não implementados. Subclasses de uma classe abstrata são obrigadas a implementar esses métodos.

``` python

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # Erro: Não é possível instanciar uma classe abstrata
rect = Rectangle(4, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


```

## 6. Composição
A composição é um conceito em que uma classe é composta de uma ou mais instâncias de outras classes. Em vez de herdar comportamentos, a composição permite que uma classe use funcionalidades de outra classe como parte de sua implementação. Isso promove a modularidade e reutilização de código.

``` python

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composição

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())


```

## 7. Coleções de Objetos
Em POO, é comum trabalhar com coleções de objetos, como listas ou dicionários. Isso permite armazenar, organizar e manipular múltiplos objetos de forma eficiente. Muitas vezes, iteradores ou métodos de ordenação são usados para trabalhar com essas coleções.

``` python

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []  # Lista para armazenar objetos do tipo Book

    def add_book(self, book):
        """Adiciona um livro à coleção."""
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title):
        """Remove um livro da coleção pelo título."""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_books(self):
        """Lista todos os livros na coleção."""
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")

# Exemplo de uso
library = Library()

# Criando objetos do tipo Book
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Adicionando livros à biblioteca
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Listando os livros
library.list_books()

# Removendo um livro
library.remove_book("1984")

# Listando os livros novamente
library.list_books()


```

## 8. Abstração
A abstração é o processo de simplificar um sistema, mostrando apenas os detalhes essenciais enquanto esconde as complexidades. Em POO, isso é feito por meio de classes e métodos que representam conceitos de forma simplificada, deixando os detalhes internos ocultos.

## Vantagens da POO
- **Reutilização de código**: A herança e a composição permitem reaproveitar estruturas e comportamentos.
- **Modularidade**: O código é organizado em pequenas partes, facilitando manutenção e leitura.
- **Escalabilidade**: Com a abstração e o encapsulamento, é possível criar sistemas que crescem sem perda de organização.
- **Facilidade de manutenção**: Alterações podem ser feitas em partes específicas sem impactar o sistema como um todo.

## Conclusão
A POO é um poderoso paradigma que organiza o desenvolvimento de software em torno de objetos e suas interações. Ao utilizar princípios como herança, polimorfismo, encapsulamento e composição, é possível criar sistemas robustos, reutilizáveis e escaláveis. Combinado com boas práticas, esse paradigma é amplamente usado em diversos contextos, desde sistemas pequenos até grandes aplicações empresariais.
