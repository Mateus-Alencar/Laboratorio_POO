#Exercício: Sistema de Controle de Funcionários
#Crie um sistema que gerencie funcionários de uma empresa. 
#Cada funcionário possui um nome, cargo e salário. 
#A empresa pode contratar novos funcionários, listar os funcionários atuais e calcular a folha de pagamento total.

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R$ {self.salario:.2f}"


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"{funcionario.nome} foi contratado como {funcionario.cargo}.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            print(f"\nFuncionários da empresa {self.nome}:")
            for funcionario in self.funcionarios:
                print(funcionario)

    def calcular_folha_pagamento(self):
        total = sum(func.salario for func in self.funcionarios)
        print(f"\nTotal da folha de pagamento: R$ {total:.2f}")


# Testando o sistema
empresa = Empresa("Tech Solutions")

# Criando funcionários
func1 = Funcionario("Mateus Alencar", "Desenvolvedor", 5000)
func2 = Funcionario("Ana Souza", "Designer", 4500)
func3 = Funcionario("Carlos Lima", "Gerente", 8000)

# Contratando funcionários
empresa.contratar_funcionario(func1)
empresa.contratar_funcionario(func2)
empresa.contratar_funcionario(func3)

# Listando funcionários
empresa.listar_funcionarios()

# Calculando folha de pagamento
empresa.calcular_folha_pagamento()
